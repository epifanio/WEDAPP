import panel as pn
#pn.extension()
pn.extension('tabulator')

from bokeh.plotting import figure
from bokeh.models.widgets.tables import NumberFormatter, BooleanFormatter, StringFormatter, DateFormatter
import pandas as pd
from wed_map import getMap, location_description
from pg_init import init_pg_db
import psycopg2


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




def intro_text(lang='en'):
    if lang == 'en':
        text = """ <h1> We're getting married - Come celebrate with us!	</h1> <br>
        <p style="font-family:'Courier New'; font-size:20px;"> A brief ceremony will take place at the Retiro District Hall at 11:00.<br>
        A grand banquet will follow at the fabulous Seeds Restaurant at 14:00. <br>
        Psst! We'll provide transportation from the district hall.<br>
        There will be friends, music, snacks, and other surprises waiting for us well into the evening. <br>
        Join us anytime!<br>
        And for those of you who can handle it, there will be a post-wedding party at the Black Jack Club <br>
        (better known to some of us as the Cat Temple) at 22:00.<br>
        All this and much more await you if you join us on <b>June 15, 2024</b>.<br>
        We have created this app so that you can sign up for the various parts of the event as well as provide <br>
        all the information we need to make that day perfect for you too.<br>
        We look forward to your presence!	</p><br>
        <center> <h4> <i>Massi & Geno	</center> </h4> </i><br>
        PS: Please, send us back your responses to the questionnaire by June 1st!"""
    if lang == 'es':
        text = """ <h1> Nos casamos - Ven a celebrarlo con nosotros! </h1> <br>
        <p style="font-family:'Courier New'; font-size:20px;"> Una sencilla ceremonia tendrá lugar en la Junta Municipal de Distrito de Retiro a las 11:00.<br>
        Le seguirá un gran banquete en el fabuloso Restaurante Seeds, a partir de las 14:00. <br>
        Pssst! Os ponemos el transporte desde la Junta de Distrito.<br>
        Allí pasaremos toda la tarde entre amigos, música, refrigerios, y alguna que otra sorpresa. <br>
        Únete en cualquier momento!.<br>
        Y a los que tengáis más aguante, os vemos en la fiesta post-boda en el club Black Jack <br>
        (más conocido para los allegados como el Templo del Gato) a partir de las 22:00.<br>
        Todo esto y mucho más tendrá lugar el día <b>15 de junio de 2024</b>.<br>
        Hemos creado esta applicación para que os podáis apuntar a las distintas partes de evento así como para trasladarnos <br>
        toda la información que nos hacen falta para que todo sea perfecto ese día, también para tí.<br>
        Os esperamos ansiosos! </p><br>
        <center> <h4> <i>Massi & Geno </center> </h4> </i><br>
        PD: Por favor, mandadnos las respuestas del cuestionario antes del 1 de junio!"""
    if lang == 'it':
        text = """ <h1> Ci stiamo sposando. Vieni a festeggiare con noi! </h1> <br>
        <p style="font-family:'Courier New'; font-size:20px;"> Una breve cerimonia si svolgerà presso la sala distrettuale della giunta municipale de El Retiro alle 11:00.<br>
        Seguirà un grande banchetto al fabuloso ristorante Seeds alle 14:00. <br>
        Forniremo il trasporto dalla sala distrettuale.<br>
        Ci saranno amici, musica, snack e altre sorprese che ci aspettano fino alla sera. <br>
        Unisciti a noi in qualsiasi momento!<br>
        E per quelli di voi che riescono a gestirlo, ci sarà una festa post-matrimonio al Black Jack Club <br>
        (più conosciuto da alcuni di noi come il Tempio del Gatto) alle 22:00.<br>
        Tutto questo e molto altro ti aspetta se ti unisci a noi il <b>15 giugno 2024</b>.<br>
        Abbiamo creato questa app in modo da poter iscriversi alle varie parti dell'evento e fornire <br>
        tutte le informazioni di cui abbiamo bisogno per rendere quella giornata perfetta anche per voi.<br>
        Aspettiamo la vostra presenza!</p><br>
        <center> <h4> <i>Massi & Geno </center> </h4> </i><br>
        PD: Per favore, provate a rispondere al questionario entro il primo di Giugno!"""
    return text
    
styles = {
    'background-color': '#F6F6F6', 'border': '1px solid grey',
    'border-radius': '5px', 'padding': '10px'
}

def form_description_text(lang='en'):
    if lang == 'en':
        text = """ <h3>The big, fat spanish-italian wedding itself:</h3> <br> 
        Remember to add, one by one, all the participants in your party """
    if lang == 'es':
        text = """ <h3> El bodorrio en sí: todo lo que incluye </h3><br> 
        Añade uno a uno a todos los participantes que vengan contigo y todas sus respuestas"""
    if lang == 'it':
        text = """<h3>Il nostro matrimonio: tutto ciò che comprende </h3><br>
         Ricordati di aggiungere, uno per uno, tutti i partecipanti che verranno con te """
    return text





html_intro_pane = pn.pane.HTML(intro_text(lang='en'), styles=styles)

html_form_pane = pn.pane.HTML(form_description_text(lang='en'), styles=styles)



name_label = pn.pane.HTML('Name', width=75)
name = pn.widgets.TextInput(name='', placeholder='...')

surname_label = pn.pane.HTML('Surname', width=75)
surname = pn.widgets.TextInput(name='', placeholder='...')

age_options_label = pn.pane.HTML('Age', width=75)
age_options = pn.widgets.Select(name='', options=['< 4', '4 - 8', '9 - 12', '> 12'], description='Age')

cerimony = pn.widgets.Checkbox(name="Yes, I will attend the ceremony at the district hall") # (Note, space is limited!)

banquet = pn.widgets.Checkbox(name="Yes, of course, I will attend the banquet!") # some question
transportation = pn.widgets.Checkbox(name="Yes, please take me from the district hall to the banquet venue")

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
    table_name = 'guest'

    # Loop over each row in the DataFrame
    for _, row in df_widget.value.iterrows():
        # Prepare the SQL query for insertion
        insert_query = f"""
            INSERT INTO {table_name} (
                Name, Surname, Age, Cerimony, Banquet, Transportation,
                Food_restrictions, Food_restrictions_details, Allergy,
                Allergy_details, Party, Friday_lunch, Friday_dinner,
                Hotel, Room_details, Days, Guest
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """
        # Extract values from the current row
        values = (
            row['Name'], row['Surname'], row['Age'], row['Cerimony'], row['Banquet'],
            row['Transportation'], row['Food restrictions'], row['Food restrictions details'],
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
    select_query = "SELECT * FROM guest"

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


party = pn.widgets.Checkbox(name="Yes, I'm game for the post-wedding party!") # (Note, adult only!)

# form.foot_note.value = "<b><font color='red'>*: a proprio carico</b><br><b><font color='red'>**: solo per maggiorenni</b>"

partecipation = pn.Column(pn.Row(name_label, name), 
                    pn.Row(surname_label, surname), 
                    pn.Row(age_options_label, age_options), 
                    pn.Row(cerimony, foot_note_1), 
                    banquet,
                    transportation, 
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


def default_separator_text(lang='en'):
    if lang == 'en':
        text = """<p><h2><b>The big, fat spanish-italian wedding itself: what's included</b></h2></p>
        <hr style="height: 5px; background-color: #3498db;">"""
    if lang == 'es':
        text = """<p><h2><b>El bodorrio en sí: todo lo que incluye</b></h2></p>
        <hr style="height: 5px; background-color: #3498db;">"""
    if lang == 'it':
        text = """<p><h2><b>Il nostro grosso grasso matrimonio: cosa include</b></h2></p>
        <hr style="height: 5px; background-color: #3498db;">"""
    return text

def optional_separator_text(lang='en'):
    if lang == 'en':
        text = """<p><h3><b>Logistic support and bits not included</b></h3></p>
        <hr style="height: 5px; background-color: #3498db;">"""
    if lang == 'es':
        text = """<p><h3><b>Apoyo logístico a y cosas que no están incluidas</b></h3></p>
        <hr style="height: 5px; background-color: #3498db;">"""
    if lang == 'it':
        text = """<p><h3><b>Appoggio logistico e cose che non sono incluse</b></h3></p>
        <hr style="height: 5px; background-color: #3498db;">"""
    return text

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
    'Transportation': BooleanFormatter(),
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
    data = {
        'Name': name.value,
        'Surname': surname.value,
        'Age': age_options.value,
        'Cerimony': cerimony.value,
        'Banquet': banquet.value,
        'Transportation': transportation.value,
        'Food restrictions': food_restrictions.value,
        'Food restrictions details': food_restrictions_details.value,
        'Allergy': allergy.value,
        'Allergy details': allergy_details.value,
        'Party': party.value,
        'Friday lunch': lunch.value,
        'Friday dinner': dinner.value,
        'Hotel': hotel.value,
        'Room details': room.value,
        'Days': date_range_picker.value,
        'Guest': number_guest.value
    }
    print(data)
    return data


df = pd.DataFrame({
        'Name': [],
        'Surname': [],
        'Age': [],
        'Cerimony': [],
        'Banquet': [],
        'Transportation': [],
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

add_row = pn.widgets.Button(name="Add row")
remove_row = pn.widgets.Button(name="Remove selected rows")

submit_button = pn.widgets.Button(name="Submit", button_type='primary')
fetch_data_button = pn.widgets.Button(name="Fetch data logger")

def change_data(data):
    data = get_data()
    # reset_data()
    #df.loc[:] = df_widget.value      
    df_widget.value.reset_index(inplace=True, drop=True)
    df_widget.value.loc[len(df_widget.value.index)] = data
    df_widget.value = df_widget.value.drop(df_widget.selection)
    
    
def remove_selected_rows(_):
    #df.drop(df_widget.selection, inplace=True)
    #df_widget.value = df.drop()
    df_widget.value = df_widget.value.drop(df_widget.selection)
    #df.drop(df_widget.selection, inplace=True)
    #df.loc[:] = df_widget.value
    df_widget.value.reset_index(inplace=True, drop=True)
    
add_row.on_click(change_data)
remove_row.on_click(remove_selected_rows)

submit_button.on_click(insert_data)
fetch_data_button.on_click(fetch_data)

button_italian = pn.widgets.Button(name="IT")
button_english = pn.widgets.Button(name="EN")
button_spanish = pn.widgets.Button(name="ES")


def change_widget_labels(lang='en'):
    if lang == 'en':
        name_label.object = 'Name'
        surname_label.object = "Surname"
        age_options_label.object = "Age"
        cerimony.name = "Yes, I will attend the ceremony at the district hall"
        transportation.name = "Yes, please take me from the district hall to the banquet venue"
        banquet.name = "Yes, of course, I will attend the banquet!"
        food_restrictions.name = "Yes, I have food restrictions"
        food_restrictions_details_label.object = "Food restrictions"
        allergy.name = "Yes, I have food allergies or intolerance"
        allergy_details_label.object = "Food allergies or intolerance"
        party.name = "Yes, I'm game for the post-wedding party!"
        lunch.name = "Yes, sign me up for a midday meal on Friday, the 14th"
        dinner.name = "Yes, sign me up for an evening meal on Friday, the 14th"
        hotel.name = "Yes, help me book a room in a hotel in the vicinity of Massi and Geno's place"
        room_label.object = "Room type"
        date_range_picker_label.object = "Arrival & Departure date"
        number_guest_label.object = "Number of guest"
        foot_note_1_description.object = "<b><font color='red'>*: Note, space is limited!</b>"
        foot_note_2_description.object = "<b><font color='red'>**: Adult only!</b>"
        foot_note_3_description.object = "<b><font color='red'>***: Restaurant TBD, own expense!</b>"
        retiro_description_pane.object, restaurant_description_pane.object, casa_sposi_description_pane.object, black_jack_description_pane.object = location_description(lang='en')

        
        
    if lang == 'it':
        name_label.object = 'Nome'
        surname_label.object = "Cognome"
        age_options_label.object = "Età"
        cerimony.name = "Sì, assisterò alla cerimonia nella sala distrettuale."
        transportation.name = "Sì, mi porti dalla sala distrettuale al luogo del banchetto."
        banquet.name = "Sì, naturalmente, assisterò al banchetto!"
        food_restrictions.name = "Sì, ho esigenze alimentari particolari"
        food_restrictions_details_label.object = "Esigenze alimentari"
        allergy.name = "Sì, ho allergie o intolleranze alimentari."
        allergy_details_label.object = "Allergie o intolleranze"
        party.name = "Sì, parteciperò alla festa post-matrimonio!"
        lunch.name = "Sì, Verrò a pranzo il venerdì 14?"
        dinner.name = "Sì, Verrò a cena il venerdì 14?"
        hotel.name = "Sì, aiutami a prenotare una camera in un hotel nelle vicinanze di Massi e la casa di Geno."
        room_label.object = "Tipo di camera"
        date_range_picker_label.object = "Data di arrivo & partenza"
        number_guest_label.object = "Numero di ospiti"
        foot_note_1_description.object = "<b><font color='red'>*: Nota, lo spazio e' limitato!</b>"
        foot_note_2_description.object = "<b><font color='red'>**: Solo per adulti!</b>"
        foot_note_3_description.object = "<b><font color='red'>***: Ristorante da stabilire, spese per conto proprio!</b>"
        retiro_description_pane.object, restaurant_description_pane.object, casa_sposi_description_pane.object, black_jack_description_pane.object = location_description(lang='it')


    if lang == 'es':
        name_label.object = 'Nombre'
        surname_label.object = "Apellidos"
        age_options_label.object = "Clase de edad"
        cerimony.name = "Sí, asistiré a la ceremonia en la Junta de Distrito"
        transportation.name = "Sí, por favor, quiero que me llevéis desde la ceremonia hasta el banquete"
        banquet.name = "Sí, por supuesto que asistiré al banquete! Qué pregunta!"
        food_restrictions.name = "Sí, tengo restricciones alimentarias"
        food_restrictions_details_label.object = "Restricciones alimentarias"
        allergy.name = "Sí, tengo alguna alergia o intolerancia alimentaria"
        allergy_details_label.object = "Alergias o intolerancia"
        party.name = "Sí, iré a la fiesta post-boda. A darlo todo!"
        lunch.name = "Sí, me apunto a una comida el viernes 14" # (por cuenta propia, en un restaurante aún por decidir)
        dinner.name = "Sí, me apunto a una cena el viernes 14" # (por cuenta propia, en un restaurante aún por decidir)
        hotel.name = "Sí, me gustaría que me ayudaras a reservar hotel cerca de la casa de Massi y Geno"
        room_label.object = "Tipo de habitación"
        date_range_picker_label.object = "Dia de llegada y partida"
        number_guest_label.object = "Número de huéspedes"
        foot_note_1_description.object = "<b><font color='red'>*: Atención! Aforo limitado!</b>"
        foot_note_2_description.object = "<b><font color='red'>**: Atención! hay que ser mayor de edad para esto!</b>"
        foot_note_3_description.object = "<b><font color='red'>***: Por cuenta propia, en un restaurante aún por decidir!</b>"
        retiro_description_pane.object, restaurant_description_pane.object, casa_sposi_description_pane.object, black_jack_description_pane.object = location_description(lang='es')




def on_button_italian_clicked(_):
    html_intro_pane.object = intro_text(lang='it')
    html_form_pane.object = form_description_text(lang='it')
    html_donation_pane.object = html_donation_text(lang='it')
    default_separator.object = default_separator_text(lang='it')
    optional_separator.object = optional_separator_text(lang='it')
    change_widget_labels(lang='it')

                                       

def on_button_english_clicked(_):
    html_intro_pane.object = intro_text(lang='en')
    html_form_pane.object = form_description_text(lang='en')
    html_donation_pane.object = html_donation_text(lang='en')
    default_separator.object = default_separator_text(lang='en')
    optional_separator.object = optional_separator_text(lang='en')
    change_widget_labels(lang='en')

def on_button_spanish_clicked(_):
    html_intro_pane.object = intro_text(lang='es')
    html_form_pane.object = form_description_text(lang='es')
    html_donation_pane.object = html_donation_text(lang='es')
    default_separator.object = default_separator_text(lang='es')
    optional_separator.object = optional_separator_text(lang='es')
    change_widget_labels(lang='es')
    
    

button_italian.on_click(on_button_italian_clicked)
button_english.on_click(on_button_english_clicked)
button_spanish.on_click(on_button_spanish_clicked)


translate_buttons = pn.Row(button_italian, button_english, button_spanish)
# html_form_pane
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

def html_donation_text(lang='en'):
    text = ''
    if lang == 'en':
        text = """ <h2>Donation welcome!:</h2> <br> 
        <p style="font-family:'Courier New'; font-size:20px;"> 
        For <i>Bizum</1> use this number: <br>
        (+34) 123456789 <br>
        <br>
        For <i>Euro</i> transfer use this account number: <br> 
        ESXX XXXX XXXX XXXX XXXX XXXX <br>
        <br>
        For <i>Vipps</i> use this number: <br> 
        (+47) 123456789 <br>
        <br>
        For <i>Kroner</i> transfer use this account number: <br> 
        NOXX XXXX XXXX XXXX XXXX XXXX <br>
        <br>
        </p>"""
    if lang == 'es':
        text = """ <h2>Se admite la voluntad!:</h2> <br> 
        <p style="font-family:'Courier New'; font-size:20px;"> 
        Para hacer un <i>Bizum</1> usa este número: <br>
        (+34) 123456789 <br>
        <br>
        Para hacer una transferencia en <i>Euro</i> usa este número de cuenta: <br> 
        ESXX XXXX XXXX XXXX XXXX XXXX <br>
        <br>
        Para hacer un <i>Vipps</i> usa este número: <br> 
        (+47) 123456789 <br>
        <br>
        Para hacer una transferencia en <i>Corona noruegas</i> usa este número de cuenta: <br> 
        NOXX XXXX XXXX XXXX XXXX XXXX <br>
        <br>
        </p>"""
    if lang == 'it':
        text = """ <h2>Donazioni benvenute!:</h2> <br> 
        <p style="font-family:'Courier New'; font-size:20px;"> 
        Per <i>Bizum</1> usa questo numero: <br>
        (+34) 123456789 <br>
        <br>
        Per trasferimenti in <i>Euro</i> usa questo numero di conto: <br> 
        ESXX XXXX XXXX XXXX XXXX XXXX <br>
        <br>
        Per <i>Vipps</i> usa questo numero: <br> 
        (+47) 123456789 <br>
        <br>
        Per trasferimenti in <i>Corone Norvegesi</i> usa questo numero di conto: <br> 
        NOXX XXXX XXXX XXXX XXXX XXXX <br>
        <br>
        </p>"""
    return text



html_donation_pane = pn.pane.HTML(html_donation_text(lang='en'), styles=styles)

retiro_description, restaurant_description, casa_sposi_description, black_jack_description = location_description(lang='en')




retiro_description_pane = pn.pane.HTML(retiro_description, styles=styles, width=600)
restaurant_description_pane = pn.pane.HTML(restaurant_description, styles=styles, width=600) 
casa_sposi_description_pane = pn.pane.HTML(casa_sposi_description, styles=styles, width=600)
black_jack_description_pane = pn.pane.HTML(black_jack_description, styles=styles, width=600)

location_description_pane = pn.GridBox(*[retiro_description_pane,
             restaurant_description_pane, casa_sposi_description_pane, black_jack_description_pane], ncols=2)


tabs = pn.Tabs(('Intro', html_intro_pane), 
               ('Form', partecipation_form), 
               ('Map', pn.Column(pn.Column(leafmap), pn.pane.HTML("<b>Locations</b>"), location_description_pane)),
               ('Donations', html_donation_pane))

df_widget.disabled = True

init_pg_db()

pn.Column(translate_buttons, tabs).servable()
