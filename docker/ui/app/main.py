import panel as pn
#pn.extension()

from bokeh.plotting import figure
from bokeh.models.widgets.tables import NumberFormatter, BooleanFormatter, StringFormatter, DateFormatter
import pandas as pd
from wed_map import getMap, location_description
from pg_init import init_pg_db
import psycopg2
from datetime import datetime as dt
from jinja2 import Environment, FileSystemLoader

from translator import intro_text, default_separator_text, optional_separator_text, html_donation_text, change_widget_labels_text


from hv_css import raw_css
#template="fast"

pn.extension('tabulator', raw_css=[raw_css])

env = Environment(loader=FileSystemLoader('/app/static'))

logout = pn.widgets.Button(name="Log out")
logout.js_on_click(code="""window.location.href = './logout'""")

# gmap_retiro_url = "https://www.google.com/maps/place/Junta+Municipal+del+Distrito+de+Retiro/@40.4023436,-3.6800094,17z/data=!4m6!3m5!1s0xd422610b505fc9d:0x643675481cabd4b0!8m2!3d40.4023395!4d-3.6774345!16s%2Fg%2F11c2nw4xrl?entry=ttu"
# gmap_restaurant_url = "https://www.google.com/maps/place/Restaurante+Seeds/@40.4381732,-3.6866107,15z/data=!4m6!3m5!1s0xd42293d73d2c977:0x819dc39751a2d781!8m2!3d40.4381732!4d-3.6866107!16s%2Fg%2F11pd2xqyxl?entry=ttu"
# gmap_url_casa_sposi = "https://www.google.com/maps/place/C%2F+de+Francisco+Silvela,+27,+6+c,+Salamanca,+28028+Madrid/@40.4313076,-3.6744468,17z/data=!3m1!4b1!4m5!3m4!1s0xd4228b77a09fc2d:0x69b75571be49d39!8m2!3d40.4313035!4d-3.6718719?entry=ttu"
# gmap_url_black_jack = "https://www.google.com/maps/place/Black+Jack+Club/@40.4187465,-3.7101133,17z/data=!3m1!4b1!4m6!3m5!1s0xd4229d71079ac6d:0x1a27a5ce4dada59b!8m2!3d40.4187424!4d-3.7075384!16s%2Fg%2F11kqq9rdk9?entry=ttu"

# TODO:
# add phone numners
# add email contact
# fill the map page with graphics and details
# add an app for the photo gallery
# user needs to receive a token url to access the app
# user can upload images and videos
# user can visualize contents

global widget_labels
widget_labels = change_widget_labels_text(lang='en')
    
styles = {
    'border': '1px solid grey',
    'border-radius': '5px', 'padding': '10px',
}

table_name = 'guest_list_session3'

full_table = pn.widgets.Checkbox(name="visualize table details", visible=False)
full_table.value = True


session_started = dt.now()

html_intro_pane = pn.pane.HTML(intro_text(lang='en'), styles=styles, sizing_mode="stretch_both")

# html_form_pane = pn.pane.HTML(form_description_text(lang='en'), styles=styles)

name_label = pn.pane.HTML(widget_labels['name_label'], width=75)
name = pn.widgets.TextInput(name='', placeholder='...')

surname_label = pn.pane.HTML(widget_labels['surname_label'], width=75)
surname = pn.widgets.TextInput(name='', placeholder='...')

age_options_label = pn.pane.HTML(widget_labels['age_options_label'], width=75)
age_options = pn.widgets.Select(name='', options=['< 4', '4 - 8', '9 - 12', '> 12'], description='Age')

cerimony = pn.widgets.Checkbox(name=widget_labels['cerimony']) # (Note, space is limited!)

banquet = pn.widgets.Checkbox(name=widget_labels['banquet']) # some question

food_restrictions = pn.widgets.Checkbox(name=widget_labels['food_restrictions'])

food_restrictions_details_label = pn.pane.HTML(widget_labels['food_restrictions_details_label'], visible=False)
food_restrictions_details = pn.widgets.Select(name='', options=['No', 'Vegetarian', 'Vegan', 'No Fish', 'No pork'],  visible=False)

allergy = pn.widgets.Checkbox(name=widget_labels['allergy'])
allergy_details_label = pn.pane.HTML(widget_labels['allergy_details_label'], visible=False)
allergy_details = pn.widgets.TextInput(name='', placeholder='...', visible=False)

foot_note_1 = pn.pane.HTML("<b><font color='red'>*</b>")
foot_note_2 = pn.pane.HTML("<b><font color='red'>**</b>")
foot_note_3 = pn.pane.HTML("<b><font color='red'>***</b>")
foot_note_4 = pn.pane.HTML("<b><font color='red'>****</b>")



foot_note_1_description = pn.pane.HTML(widget_labels['foot_note_1_description'] ) 
foot_note_2_description = pn.pane.HTML(widget_labels['foot_note_2_description'] ) 
foot_note_3_description = pn.pane.HTML(widget_labels['foot_note_3_description'] ) 


def insert_data(event):
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname='mydatabase',
        user='myuser',
        password='mypassword',
        host='db'
    )

    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    # Define the table name
    # table_name = 'guest_list_session'

    # Loop over each row in the DataFrame
    for _, row in df_widget.value.iterrows():
        # Prepare the SQL query for insertion
        insert_query = f"""
            INSERT INTO {table_name} (
                Name, Surname, Age, Cerimony, Banquet,
                Food_restrictions, Food_restrictions_details, Allergy,
                Allergy_details, Party, Friday_lunch, Friday_dinner,
                Hotel, Room_details, Days, Guest, Session
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """
        # Extract values from the current row
        values = (
            row['Name'], row['Surname'], row['Age'], row['Cerimony'], row['Banquet'],
            row['Food restrictions'], row['Food restrictions details'],
            row['Allergy'], row['Allergy details'], row['Party'], row['Friday lunch'],
            row['Friday dinner'], row['Hotel'], row['Room details'], row['Days'], row['Guest'], row['Session']
        )

        # Execute the insertion query
        cursor.execute(insert_query, values)
    try:
        print("insert_query")
        print(insert_query)
        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()
        app.modal[0].clear()
        modal_3_content = pn.Row(pn.pane.HTML(widget_labels['modal_3_content']))
        app.modal[0].append(modal_3_content)
        app.open_modal()
    except UnboundLocalError:
        app.modal[0].clear()
        modal_1_content = pn.Row(pn.pane.HTML(widget_labels['modal_1_content']))
        app.modal[0].append(modal_1_content)
        app.open_modal()
    
    
def fetch_data(event):
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname='mydatabase',
        user='myuser',
        password='mypassword',
        host='db'
    )

    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    # Define the SQL query to fetch all data from the table
    select_query = f"SELECT * FROM {table_name}"
    print("select_query")
    print(select_query)
    # Execute the query
    cursor.execute(select_query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Convert the fetched data into a DataFrame
    column_names = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=column_names)

    # Display the DataFrame
    pn.state.session_info['session_started'] = session_started
    print('cookies: ', pn.state.curdoc.session_context.request.cookies)
    print('session info', pn.state.session_info)
    print(df)


def show_allergy_details(event):
    allergy_details.value = ''
    if allergy.value:
        allergy_details.visible = True
        allergy_details_label.visible = True
    else: 
        allergy_details.visible = False
        allergy_details_label.visible = False

allergy.param.watch(show_allergy_details, 'value')

def show_food_restrictions_details(event):
    food_restrictions_details.value = 'No'
    if food_restrictions.value:
        food_restrictions_details_label.visible = True
        food_restrictions_details.visible = True
    else: 
        food_restrictions_details_label.visible = False
        food_restrictions_details.visible = False

food_restrictions.param.watch(show_food_restrictions_details, 'value')


party = pn.widgets.Checkbox(name=widget_labels['party']) # (Note, adult only!)

partecipation = pn.Column(pn.Row(name_label, name), 
                    pn.Row(surname_label, surname), 
                    pn.Row(age_options_label, age_options), 
                    pn.Row(cerimony, foot_note_1), 
                    banquet,
                    pn.Column(food_restrictions, pn.Row(pn.Spacer(width=100), food_restrictions_details_label, food_restrictions_details)), 
                    pn.Column(allergy, pn.Row(pn.Spacer(width=100), pn.Column(allergy_details_label, allergy_details))), 
                    pn.Row(party, foot_note_2))

lunch = pn.widgets.Checkbox(name = widget_labels['lunch']) # (restaurant TBD, own expense!)
dinner = pn.widgets.Checkbox(name = widget_labels['dinner']) # (restaurant TBD, own expense!)

hotel = pn.widgets.Checkbox(name=widget_labels['hotel']) # (para tus acompañantes, puedes responder "no")
room_label = pn.pane.HTML(widget_labels['room_label'], visible=False)
room = pn.widgets.Select(name='', options=['Single', 'Double', 'Family'], visible=False)
date_range_picker_label = pn.pane.HTML(widget_labels['date_range_picker_label'], visible=False)
date_range_picker = pn.widgets.DateRangePicker(name='', visible=False)
number_guest_label = pn.pane.HTML(widget_labels['number_guest_label'], visible=False)
number_guest = pn.widgets.IntInput(name='', value=0, step=1, start=0, end=10, visible=False)


def show_accomodation_details(event):
    room.value = 'Single'
    # date_range_picker
    number_guest.value = 0
    if hotel.value:
        room_label.visible = True
        room.visible = True
        number_guest.visible = True
        number_guest_label.visible = True
        date_range_picker.visible = True
        date_range_picker_label.visible = True
    else: 
        room_label.visible = False
        room.visible = False
        number_guest_label.visible = False
        number_guest.visible = False
        date_range_picker_label.visible = False
        date_range_picker.visible = False

hotel.param.watch(show_accomodation_details, 'value')


default_separator = pn.pane.HTML(default_separator_text(lang='en'), width=600)

optional_separator = pn.pane.HTML(optional_separator_text(lang='en'), width=600)

extra = pn.Column(pn.Row(lunch, foot_note_3), 
                  pn.Row(dinner, foot_note_3), 
                  hotel, 
                  pn.Row(pn.Spacer(width=100), 
                         pn.Column(room_label, 
                                   room, 
                                   date_range_picker_label, 
                                   date_range_picker, 
                                   number_guest_label, 
                                   number_guest)),
                  )



bokeh_formatters = {
    'Name': StringFormatter(),
    'Surname': StringFormatter(),
    'Age': StringFormatter(),
    'Cerimony': BooleanFormatter(),
    'Banquet': BooleanFormatter(),
    'Food restrictions': BooleanFormatter(),
    'Food restrictions details': StringFormatter(),
    'Allergy': BooleanFormatter(),
    'Allergy details': StringFormatter(),
    'Party': BooleanFormatter(),
    'Friday lunch': BooleanFormatter(),
    'Friday dinner': BooleanFormatter(),
    'Hotel': BooleanFormatter(),
    'Room details': StringFormatter(),
    'Days': StringFormatter(),
    'Guest': NumberFormatter(),
    'Session': StringFormatter(),
}

def get_data():
    if hotel.value:
        date_range = date_range_picker.value
        room_details = room.value
        guests = number_guest.value
    else:
        date_range = ''
        room_details = ''
        guests = 0
    data = {
        'Name': name.value,
        'Surname': surname.value,
        'Age': age_options.value,
        'Cerimony': cerimony.value,
        'Banquet': banquet.value,
        'Food restrictions': food_restrictions.value,
        'Food restrictions details': food_restrictions_details.value,
        'Allergy': allergy.value,
        'Allergy details': allergy_details.value,
        'Party': party.value,
        'Friday lunch': lunch.value,
        'Friday dinner': dinner.value,
        'Hotel': hotel.value,
        'Room details': room_details,
        'Days': date_range,
        'Guest': guests,
        'Session': session_started
    }
    print(data)
    return data


df = pd.DataFrame({
        'Name': [],
        'Surname': [],
        'Age': [],
        'Cerimony': [],
        'Banquet': [],
        'Food restrictions': [],
        'Food restrictions details': [],
        'Allergy': [],
        'Allergy details': [],
        'Party': [],
        'Friday lunch': [],
        'Friday dinner': [],
        'Hotel': [],
        'Room details': [],
        'Days': [],
        'Guest': [],
        'Session': [],
}, index=[])

df_widget = pn.widgets.Tabulator(df, formatters=bokeh_formatters)
# df_widget.hidden_columns = ['index', 'Session']

df_widget.hidden_columns = ['index', 
                                    'Session', 
                                    'Age', 
                                    'Cerimony', 
                                    'Banquet', 
                                    'Food restrictions', 
                                    'Food restrictions details', 
                                    'Allergy', 
                                    'Allergy details', 
                                    'Allergy details',
                                    'Party',
                                    'Friday lunch',
                                    'Friday dinner',
                                    'Hotel',
                                    'Room details',
                                    'Days',
                                    'Guest',
                                    'Session']

add_row = pn.widgets.Button(name="Add New Record")
remove_row = pn.widgets.Button(name="Remove Selected Record")

show_details = pn.widgets.Button(name="Show Table details")

submit_button = pn.widgets.Button(name="Submit Records", button_type='primary')
fetch_data_button = pn.widgets.Button(name="Fetch data logger")


def show_table_details(event):
    print(full_table.value)
    if full_table.value:
        df_widget.hidden_columns = ['index', 'Session']
        full_table.value = False
    else: 
        df_widget.hidden_columns = ['index', 
                                    'Session', 
                                    'Age', 
                                    'Cerimony', 
                                    'Banquet', 
                                    'Food restrictions', 
                                    'Food restrictions details', 
                                    'Allergy', 
                                    'Allergy details', 
                                    'Allergy details',
                                    'Party',
                                    'Friday lunch',
                                    'Friday dinner',
                                    'Hotel',
                                    'Room details',
                                    'Days',
                                    'Guest',
                                    'Session']
        full_table.value = True
    print('meta_viewport: ', app.meta_viewport)


def reset_widgets_values(event):
    name.value = ''
    surname.value = ''
    age_options.value = ''
    cerimony.value = False
    banquet.value = False
    food_restrictions.value = False
    food_restrictions_details.value = ''
    allergy.value = False
    allergy_details.value = ''
    party.value = False
    lunch.value = False
    dinner.value = False
    hotel.value = False
    room.value = 'Single'
    #try:
    #     date_range_picker.value = (session_started, session_started)
    #     date_range_picker.start = None
    #     date_range_picker.end = None
    # except ValueError:
    #     print("failing to reset data time picker widget")
    number_guest.value = 0


def change_data(data):
    # Add a check if mandatory values are set
    # if not, raise a modal dialog to warn about the missing mandatory values
    data = get_data()
    print(data)
    if data['Name'] == '' or data['Surname'] == '': 
        app.modal[0].clear()
        modal_0_content = pn.Row(pn.pane.HTML(widget_labels['modal_0_content']))
        app.modal[0].append(modal_0_content)
        app.open_modal()
        print(modal_0_content)
        print(widget_labels['modal_0_content'])
        return
    # reset_data()
    #df.loc[:] = df_widget.value      
    df_widget.value.reset_index(inplace=True, drop=True)
    df_widget.value.loc[len(df_widget.value.index)] = data
    df_widget.value = df_widget.value.drop(df_widget.selection)
    # reset_widgets_values()
    try:
    #    date_range_picker.value = (session_started, session_started)
        date_range_picker.value = (None, None)
    #    date_range_picker.start = None
    #    date_range_picker.end = None
    except ValueError as e:
        print(f"failing to reset data time picker widget, exception was: {e}")
    

def remove_selected_rows(_):
    #df.drop(df_widget.selection, inplace=True)
    #df_widget.value = df.drop()
    # check if a row or more is selected
    if len(df_widget.selection) == 0:
        app.modal[0].clear()
        modal_4_content = pn.Row(pn.pane.HTML(widget_labels['modal_4_content']))
        app.modal[0].append(modal_4_content)
        app.open_modal()
        return
    df_widget.value = df_widget.value.drop(df_widget.selection)
    #df.drop(df_widget.selection, inplace=True)
    #df.loc[:] = df_widget.value
    df_widget.value.reset_index(inplace=True, drop=True)
    
add_row.on_click(change_data)
add_row.on_click(reset_widgets_values)

show_details.on_click(show_table_details)

remove_row.on_click(remove_selected_rows)

submit_button.on_click(insert_data)

fetch_data_button.on_click(fetch_data)

button_italian = pn.widgets.Button(name="IT")
button_english = pn.widgets.Button(name="EN")
button_spanish = pn.widgets.Button(name="ES")

modal_0_content = pn.Row(pn.pane.HTML(widget_labels['modal_0_content']))
modal_1_content = pn.Row(pn.pane.HTML(widget_labels['modal_1_content']))
modal_2_content = pn.Row(pn.pane.HTML(widget_labels['modal_2_content']))
modal_3_content = pn.Row(pn.pane.HTML(widget_labels['modal_3_content']))
modal_4_content = pn.Row(pn.pane.HTML(widget_labels['modal_4_content']))

# modal_btn = pn.widgets.Button(name="Click for modal")

def open_modal_0(event):
    app.modal[0].clear()
    modal_0_content = pn.Row(pn.pane.HTML(widget_labels['modal_0_content']))
    app.modal[0].append(modal_0_content)
    app.open_modal()
    
def open_modal_1(event):
    app.modal[0].clear()
    modal_1_content = pn.Row(pn.pane.HTML(widget_labels['modal_1_content']))
    app.modal[0].append(modal_1_content)
    app.open_modal()

def open_modal_2(event):
    app.modal[0].clear()
    modal_2_content = pn.Row(pn.pane.HTML(widget_labels['modal_2_content']))
    app.modal[0].append(modal_2_content)
    app.open_modal()

def open_modal_3(event):
    app.modal[0].clear()
    modal_3_content = pn.Row(pn.pane.HTML(widget_labels['modal_3_content']))
    app.modal[0].append(modal_3_content)
    app.open_modal()
    
def open_modal_4(event):
    app.modal[0].clear()
    modal_4_content = pn.Row(pn.pane.HTML(widget_labels['modal_4_content']))
    app.modal[0].append(modal_4_content)
    app.open_modal()
# modal_btn.on_click(open_modal)


def change_widget_labels(lang='en'):
    global widget_labels
    widget_labels = change_widget_labels_text(lang=lang)
    name_label.object = widget_labels['name_label']
    surname_label.object = widget_labels['surname_label']
    age_options_label.object = widget_labels['age_options_label']
    cerimony.name = widget_labels['cerimony']
    banquet.name = widget_labels['banquet']
    food_restrictions.name = widget_labels['food_restrictions']
    food_restrictions_details_label.object = widget_labels['food_restrictions_details_label']
    allergy.name = widget_labels['allergy']    
    allergy_details_label.object = widget_labels['allergy_details_label']   
    party.name = widget_labels['party'] 
    lunch.name = widget_labels['lunch'] 
    dinner.name = widget_labels['dinner'] 
    hotel.name = widget_labels['hotel'] 
    room_label.object = widget_labels['room_label'] 
    date_range_picker_label.object = widget_labels['date_range_picker_label'] 
    number_guest_label.object = widget_labels['number_guest_label'] 
    foot_note_1_description.object = widget_labels['foot_note_1_description'] 
    foot_note_2_description.object = widget_labels['foot_note_2_description'] 
    foot_note_3_description.object = widget_labels['foot_note_3_description'] 
    retiro_description_pane.object = widget_labels['retiro_description_pane']
    restaurant_description_pane.object = widget_labels['restaurant_description_pane']
    casa_sposi_description_pane.object = widget_labels['casa_sposi_description_pane']
    black_jack_description_pane.object = widget_labels['black_jack_description_pane']
    modal_0_content.object= widget_labels['modal_0_content']
    modal_1_content.object= widget_labels['modal_1_content']
    modal_2_content.object= widget_labels['modal_2_content']
    modal_3_content.object= widget_labels['modal_3_content']
    modal_4_content.object= widget_labels['modal_4_content']


def on_button_italian_clicked(_):
    change_widget_labels(lang='it')
    html_intro_pane.object = intro_text(lang='it')
    html_donation_pane.object = html_donation_text(lang='it')
    default_separator.object = default_separator_text(lang='it')
    optional_separator.object = optional_separator_text(lang='it')
        

def on_button_english_clicked(_):
    change_widget_labels(lang='en')
    html_intro_pane.object = intro_text(lang='en')
    html_donation_pane.object = html_donation_text(lang='en')
    default_separator.object = default_separator_text(lang='en')
    optional_separator.object = optional_separator_text(lang='en')



def on_button_spanish_clicked(_):
    change_widget_labels(lang='es')
    html_intro_pane.object = intro_text(lang='es')
    html_donation_pane.object = html_donation_text(lang='es')
    default_separator.object = default_separator_text(lang='es')
    optional_separator.object = optional_separator_text(lang='es')

    

button_italian.on_click(on_button_italian_clicked)
button_english.on_click(on_button_english_clicked)
button_spanish.on_click(on_button_spanish_clicked)

translate_buttons = pn.Row(button_italian, button_english, button_spanish)

partecipation_form = pn.Column(default_separator, 
                               partecipation, 
                               optional_separator, 
                               extra, 
                               df_widget, 
                               pn.Row(add_row, 
                                      remove_row, show_details, submit_button), 
                               fetch_data_button,
                               pn.Spacer(height=20),
                               foot_note_1_description,
                               foot_note_2_description,
                               foot_note_3_description, height=1200)

leafmap = getMap()

html_donation_pane = pn.pane.HTML(html_donation_text(lang='en'), styles=styles)

retiro_description, restaurant_description, casa_sposi_description, black_jack_description = location_description(lang='en')

retiro_description_pane = pn.pane.HTML(retiro_description, styles=styles, width=525)

restaurant_description_pane = pn.pane.HTML(restaurant_description, styles=styles, width=525) 
casa_sposi_description_pane = pn.pane.HTML(casa_sposi_description, styles=styles, width=525)
black_jack_description_pane = pn.pane.HTML(black_jack_description, styles=styles, width=525)

location_description_pane = pn.GridBox(*[retiro_description_pane,
             restaurant_description_pane, casa_sposi_description_pane, black_jack_description_pane], ncols=1)


tabs = pn.Tabs((' Intro ', html_intro_pane), 
               (' Form ', partecipation_form), 
               (' Map ', pn.Column(pn.Column(leafmap), 
                                 pn.pane.HTML("""<p style="font-family:'Courier New'; font-size:25px;"><b>Locations</b></p>"""), 
                                 location_description_pane, sizing_mode='stretch_both')),
               (' Bank details ', html_donation_pane), dynamic=True)

df_widget.disabled = True

init_pg_db(table_name)


jinja_template = env.get_template('template.html')
tmpl = pn.Template(jinja_template)

#tmpl.modal.append("## This is a modal")

# Create a button
#modal_btn = pn.widgets.Button(name="Click for modal")

# tmpl.add_panel('A', pn.Column(logout, translate_buttons, tabs))
# tmpl.add_variable('app_title', '<center><h1>♥ Geno & Massi Sposi! ♥</h1></center>')
# tmpl.servable('Geno & Massi Sposi!')

# widgets = pn.Column(f"Congrats `{pn.state.user}`. You got access!", logout, pn.Column(translate_buttons, tabs))
widgets = pn.Column(pn.Column(pn.Row(translate_buttons, logout), tabs))

# app.servable()

# modal_1_content = pn.Row(pn.pane.Markdown("## This is a modal"))
# modal_btn = pn.widgets.Button(name="Click for modal")

# def open_modal(event):
#     app.modal[0].clear()
#     app.modal[0].append(modal_1_content)
#     app.open_modal()
    
# modal_btn.on_click(open_modal)


app = pn.template.FastListTemplate(
    site="♥", title="Geno & Massi Sposi!",
    main=[widgets],
    meta_viewport = "width=device-width,minimum-scale=1,initial-scale=1"
)

app.modal.append(pn.Column())

app.modal[0].clear()
app.modal[0].append(modal_1_content)

# app.main[0].append(modal_btn)

app.servable()

print(dir(app))
print(app.meta_viewport)
# pn.Column(translate_buttons, tabs).servable("Massi & Geno")
