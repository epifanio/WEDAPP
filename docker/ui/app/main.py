import panel as pn
#pn.extension()
pn.extension('tabulator')

from bokeh.plotting import figure
from bokeh.models.widgets.tables import NumberFormatter, BooleanFormatter, StringFormatter, DateFormatter
import pandas as pd
from wed_map import getMap, location_description
from pg_init import init_pg_db
import psycopg2
from datetime import datetime as dt
from jinja2 import Environment, FileSystemLoader

from translator import intro_text, default_separator_text, optional_separator_text, html_donation_text, change_widget_labels_text

env = Environment(loader=FileSystemLoader('/app/static'))

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


    
styles = {
    'background-color': '#F6F6F6', 'border': '1px solid grey',
    'border-radius': '5px', 'padding': '10px'
}



session_started = dt.now()

html_intro_pane = pn.pane.HTML(intro_text(lang='en'), styles=styles)

# html_form_pane = pn.pane.HTML(form_description_text(lang='en'), styles=styles)

name_label = pn.pane.HTML('Name', width=75)
name = pn.widgets.TextInput(name='', placeholder='...')

surname_label = pn.pane.HTML('Surname', width=75)
surname = pn.widgets.TextInput(name='', placeholder='...')

age_options_label = pn.pane.HTML('Age', width=75)
age_options = pn.widgets.Select(name='', options=['< 4', '4 - 8', '9 - 12', '> 12'], description='Age')

cerimony = pn.widgets.Checkbox(name="Yes, I will attend the ceremony at the district hall") # (Note, space is limited!)

banquet = pn.widgets.Checkbox(name="Yes, of course, I will attend the reception!") # some question

food_restrictions = pn.widgets.Checkbox(name='Yes, I have food restrictions')

food_restrictions_details_label = pn.pane.HTML('Food restrictions', visible=False)
food_restrictions_details = pn.widgets.Select(name='', options=['No', 'Vegetarian', 'Vegan', 'No Fish', 'No pork'],  visible=False)

allergy = pn.widgets.Checkbox(name='Yes, I have food allergies or intolerance')
allergy_details_label = pn.pane.HTML('Food allergies or intolerance', visible=False)
allergy_details = pn.widgets.TextInput(name='', placeholder='...', visible=False)

foot_note_1 = pn.pane.HTML("<b><font color='red'>*</b>")
foot_note_2 = pn.pane.HTML("<b><font color='red'>**</b>")
foot_note_3 = pn.pane.HTML("<b><font color='red'>***</b>")
foot_note_4 = pn.pane.HTML("<b><font color='red'>****</b>")


foot_note_1_description = pn.pane.HTML("<b><font color='red'>*: Note, space is limited!</b>") 
foot_note_2_description = pn.pane.HTML("<b><font color='red'>**: Adult only!</b>") 
foot_note_3_description = pn.pane.HTML("<b><font color='red'>***: Restaurant TBD, own expense!</b>") 


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
    table_name = 'guest_list'

    # Loop over each row in the DataFrame
    for _, row in df_widget.value.iterrows():
        # Prepare the SQL query for insertion
        insert_query = f"""
            INSERT INTO {table_name} (
                Name, Surname, Age, Cerimony, Banquet,
                Food_restrictions, Food_restrictions_details, Allergy,
                Allergy_details, Party, Friday_lunch, Friday_dinner,
                Hotel, Room_details, Days, Guest
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """
        # Extract values from the current row
        values = (
            row['Name'], row['Surname'], row['Age'], row['Cerimony'], row['Banquet'],
            row['Food restrictions'], row['Food restrictions details'],
            row['Allergy'], row['Allergy details'], row['Party'], row['Friday lunch'],
            row['Friday dinner'], row['Hotel'], row['Room details'], row['Days'], row['Guest']
        )

        # Execute the insertion query
        cursor.execute(insert_query, values)

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    
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
    select_query = "SELECT * FROM guest_list"

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


party = pn.widgets.Checkbox(name="Yes, I'm down for the after party!") # (Note, adult only!)

partecipation = pn.Column(pn.Row(name_label, name), 
                    pn.Row(surname_label, surname), 
                    pn.Row(age_options_label, age_options), 
                    pn.Row(cerimony, foot_note_1), 
                    banquet,
                    pn.Column(food_restrictions, pn.Row(pn.Spacer(width=100), food_restrictions_details_label, food_restrictions_details)), 
                    pn.Column(allergy, pn.Row(pn.Spacer(width=100), pn.Column(allergy_details_label, allergy_details))), 
                    pn.Row(party, foot_note_2))

lunch = pn.widgets.Checkbox(name='Yes, sign me up for a midday meal on Friday, the 14th') # (restaurant TBD, own expense!)
dinner = pn.widgets.Checkbox(name='Yes, sign me up for an evening meal on Friday, the 14th') # (restaurant TBD, own expense!)

hotel = pn.widgets.Checkbox(name="Yes, help me book a room in a hotel in the vicinity of Massi and Geno's place") # (para tus acompañantes, puedes responder "no")
room_label = pn.pane.HTML('Room type', visible=False)
room = pn.widgets.Select(name='', options=['Single', 'Double', 'Family'], visible=False)
date_range_picker_label = pn.pane.HTML('Arrival & Departure date', visible=False)
date_range_picker = pn.widgets.DateRangePicker(name='', visible=False)
number_guest_label = pn.pane.HTML('Number of guest', visible=False)
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
    'Guest': NumberFormatter()
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
        'Guest': guests
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
}, index=[])

df_widget = pn.widgets.Tabulator(df, formatters=bokeh_formatters)
df_widget.hidden_columns = ['index']

add_row = pn.widgets.Button(name="Add row")
remove_row = pn.widgets.Button(name="Remove selected rows")

submit_button = pn.widgets.Button(name="Submit", button_type='primary')
fetch_data_button = pn.widgets.Button(name="Fetch data logger")

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
    df_widget.value = df_widget.value.drop(df_widget.selection)
    #df.drop(df_widget.selection, inplace=True)
    #df.loc[:] = df_widget.value
    df_widget.value.reset_index(inplace=True, drop=True)
    
add_row.on_click(change_data)
add_row.on_click(reset_widgets_values)

remove_row.on_click(remove_selected_rows)

submit_button.on_click(insert_data)

fetch_data_button.on_click(fetch_data)

button_italian = pn.widgets.Button(name="IT")
button_english = pn.widgets.Button(name="EN")
button_spanish = pn.widgets.Button(name="ES")

def change_widget_labels(lang='en'):
    label_dict = change_widget_labels_text(lang=lang)
    name_label.object = label_dict['name_label']
    surname_label.object = label_dict['surname_label']
    age_options_label.object = label_dict['age_options_label']
    cerimony.name = label_dict['cerimony']
    banquet.name = label_dict['banquet']
    food_restrictions.name = label_dict['food_restrictions']
    food_restrictions_details_label.object = label_dict['food_restrictions_details_label']
    allergy.name = label_dict['allergy']    
    allergy_details_label.object = label_dict['allergy_details_label']   
    party.name = label_dict['party'] 
    lunch.name = label_dict['lunch'] 
    dinner.name = label_dict['dinner'] 
    hotel.name = label_dict['hotel'] 
    room_label.object = label_dict['room_label'] 
    date_range_picker_label.object = label_dict['date_range_picker_label'] 
    number_guest_label.object = label_dict['number_guest_label'] 
    foot_note_1_description.object = label_dict['foot_note_1_description'] 
    foot_note_2_description.object = label_dict['foot_note_2_description'] 
    foot_note_3_description.object = label_dict['foot_note_3_description'] 
    retiro_description_pane.object = label_dict['retiro_description_pane']
    restaurant_description_pane.object = label_dict['restaurant_description_pane']
    casa_sposi_description_pane.object = label_dict['casa_sposi_description_pane']
    black_jack_description_pane.object = label_dict['black_jack_description_pane']


def on_button_italian_clicked(_):
    html_intro_pane.object = intro_text(lang='it')
    html_donation_pane.object = html_donation_text(lang='it')
    default_separator.object = default_separator_text(lang='it')
    optional_separator.object = optional_separator_text(lang='it')
    change_widget_labels(lang='it')
                                    

def on_button_english_clicked(_):
    html_intro_pane.object = intro_text(lang='en')
    html_donation_pane.object = html_donation_text(lang='en')
    default_separator.object = default_separator_text(lang='en')
    optional_separator.object = optional_separator_text(lang='en')
    change_widget_labels(lang='en')


def on_button_spanish_clicked(_):
    html_intro_pane.object = intro_text(lang='es')
    html_donation_pane.object = html_donation_text(lang='es')
    default_separator.object = default_separator_text(lang='es')
    optional_separator.object = optional_separator_text(lang='es')
    change_widget_labels(lang='es')
    

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
                                      remove_row), 
                               pn.Row(submit_button, 
                                      fetch_data_button,
                                      ), 
                               pn.Spacer(height=20),
                               foot_note_1_description,
                               foot_note_2_description,
                               foot_note_3_description)

leafmap = getMap()





html_donation_pane = pn.pane.HTML(html_donation_text(lang='en'), styles=styles)

retiro_description, restaurant_description, casa_sposi_description, black_jack_description = location_description(lang='en')




retiro_description_pane = pn.pane.HTML(retiro_description, styles=styles, width=525)
restaurant_description_pane = pn.pane.HTML(restaurant_description, styles=styles, width=525) 
casa_sposi_description_pane = pn.pane.HTML(casa_sposi_description, styles=styles, width=525)
black_jack_description_pane = pn.pane.HTML(black_jack_description, styles=styles, width=525)

location_description_pane = pn.GridBox(*[retiro_description_pane,
             restaurant_description_pane, casa_sposi_description_pane, black_jack_description_pane], ncols=1)


tabs = pn.Tabs(('Intro', html_intro_pane), 
               ('Form', partecipation_form), 
               ('Map', pn.Column(pn.Column(leafmap), 
                                 pn.pane.HTML("""<p style="font-family:'Courier New'; font-size:25px;"><b>Locations</b></p>"""), 
                                 location_description_pane, sizing_mode='stretch_both')),
               ('Donations', html_donation_pane))

df_widget.disabled = True

init_pg_db()



jinja_template = env.get_template('template.html')
tmpl = pn.Template(jinja_template)


#tmpl.modal.append("## This is a modal")

# Create a button
#modal_btn = pn.widgets.Button(name="Click for modal")

tmpl.add_panel('A', pn.Column(translate_buttons, tabs))
tmpl.add_variable('app_title', '<center><h1>Geno & Massi Sposi!</h1></center>')
tmpl.servable()

# pn.Column(translate_buttons, tabs).servable("Massi & Geno")
