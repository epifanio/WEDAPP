from wed_map import location_description

def intro_text(lang='en'):
    if lang == 'en':
        text = """  <center> <h1>WE’RE FINALLY GETTING MARRIED!!!</h1></center> 
        <br>
        <br>
        <p style="font-family:'Courier New';">To celebrate, we have arranged a touristic, 
        gastronomic wedding crawl that we hope you’ll enjoy. 
        These are the main stops:<br>
        <br>
        <b>11:00 Retiro District Hall.</b> A brief ceremony will take place here, 
        followed by a stimulating walk to work up an appetite.<br>
        <br>
        <b>12:00 Paseo del Prado 48.</b> Fear not! From this point on we’ll be on wheels.<br>
        <br>
        <b>14:00 Seeds Restaurant.</b> 
        The reception will include a grand banquet and a surprise-packed afternoon.<br>
        <br>
        <b>22:00 Black Jack Club</b> (better known to us hard-core Madridians as the Cat Temple). 
        Those of you who can handle it are invited to join us there for the after party!<br>
        <br>
        See you on <b>June 15, 2024!</b><br>
        <br>
        We have created this awesome trilingual app so that you can confirm your attendance, 
        as well as provide us with all the information we need to make that day perfect for you too.<br>
        <br>
        <br>
         <h2 align="center">♥ Geno & Massi  ♥</h2>
        <br>
        <br>
        <br></p>
        <p style="font-family:'Courier New'; font-size:15px;"><b><font color='orange'> P.S.: <br> Please, fill in the form by June 1st! </b></p>"""
        
    if lang == 'es':
        text = """  <center> <h1>POR FIN NOS CASAMOS!!!</h1></center> 
        <br>
        <br>
        <p style="font-family:'Courier New';">Para celebrarlo 
        hemos preparado un un recorrido turísitico-gastronómico-nupcial al que esperamos que te unas. 
        Estas son las paradas:<br>
        <br>
        <b>11:00 Junta Municipal de Distrito de Retiro.</b> Aquí tendrá lugar una sencilla ceremonia 
        seguida de un estimulante paseo para abrir el apetito.<br>
        <br>
        <b>12:00 Paseo del Prado 48.</b> ¡No temáis! A partir de este momento iremos motorizados.<br>
        <br>
        <b>14:00 Restaurante Seeds.</b> 
        Allí se celebrará un banquete por todo lo alto con sobremesa llena de sorpresas.<br>
        <br>
        <b>22:00 Club Black Jack</b> (más conocido para los allegados como el Templo del Gato). 
        A los que tengáis más aguante, os vemos ahí, en la fiesta post-boda!<br>
        <br>
        Nos vemos el <b>15 de junio de 2024</b> en alguno de estos puntos de encuentro!<br>
        <br>
        Hemos creado esta pedazo de applicación tri-lingüe para que nos puedas confirmar tu asistencia, 
        así como para trasladarnos toda la información que nos hacen falta para que todo sea perfecto ese día, 
        también para tí!<br>
        <br>
        <br>
        Os esperamos ansiosos!
        <br>
        <br>
         <h2 align="center">♥ Geno & Massi ♥</h2>
        <br>
        <br>
        <br></p>
        <p style="font-family:'Courier New'; font-size:15px;"><b><font color='orange'> P.D.: <br> Por favor, 
        mandadnos las respuestas del formulario antes del 1 de junio! </b></p>"""
    if lang == 'it':
        text = """<center> <h1>FINALMENTE CI SPOSIAMO!!!</h1></center> 
        <br>
        <br>
        <p style="font-family:'Courier New';">Per celebrarlo 
        abbiamo preparato un tour turistico eno-gastronomico nuziale a cui speriamo ti unirai. 
        Queste sono le tappe:<br>
        <br>
        <b>11:00 Distretto municipale "El Retiro".</b> Qui avrà luogo una semplice cerimonia 
        seguita da una stimolante passeggiata per aprire l'appetito.<br>
        <br>
        <b>12:00 Paseo del Prado 48.</b> Non temete! Da questo momento andremo motorizzati.<br>
        <br>
        <b>14:00 Ristorante Seeds.</b> 
        Qui si terrà un sontuoso banchetto con una dopo cena piena di sorprese.<br>
        <br>
        <b>22:00 Black Jack Club</b> (più conosciuto dagli intimi come il Tempio del Gatto). 
        A coloro che resisteranno, ci vediamo lì, alla festa post-matrimonio!<br>
        <br>
        Ci vedremo il <b>15 giugno 2024</b> in uno dei punti di incontro!<br>
        <br>
        Abbiamo creato questa favolosa applicazione tri-lingue affinché tu possa confermare la tua presenza, 
        così come per fornirci tutte le informazioni di cui abbiamo bisogno per rendere perfetto questo giorno, 
        anche per te!<br>
        <br>
        <br>
        Vi aspettiamo con impazienza!
        <br>
        <br>
         <h2 align="center">♥ Geno & Massi ♥</h2>
        <br>
        <br>
        <br></p>
        <p style="font-family:'Courier New'; font-size:15px;"><b><font color='orange'> P.S.: <br> Per favore, 
        inviateci le risposte al modulo entro il 1 giugno! </b></p>"""
    return text

def default_separator_text(lang='en'):
    if lang == 'en':
        text = """ <p><h2><b> The big, fat italo-spanish wedding: what's included </b></h2></p>
        <hr style="height: 5px; background-color: #3498db;">
        Remember to add all your details, as well as the details of all members of your party"""
    if lang == 'es':
        text = """ <p><h2><b> El bodorrio: todo lo que incluye </b></h2></p>
        <hr style="height: 5px; background-color: #3498db;">
        Acuérdate de agregar los datos de todos tus acompañantes, así como los tuyos propios, de uno en uno"""
    if lang == 'it':
        text = """<p><h2><b> Il Matrimonio: Tutto ciò che Include </b></h2></p>
        <hr style="height: 5px; background-color: #3498db;">
        Ricorda di aggiungere i dati di tutti i tuoi accompagnatori, così come i tuoi, uno per uno. """
    return text

def optional_separator_text(lang='en'):
    if lang == 'en':
        text = """<p><h2><b>Logistic support and bits not included</b></h2></p>
        <hr style="height: 5px; background-color: #3498db;">"""
    if lang == 'es':
        text = """<p><h2><b>Apoyo logístico y cosas que no están incluidas</b></h2></p>
        <hr style="height: 5px; background-color: #3498db;">"""
    if lang == 'it':
        text = """<p><h2><b>Appoggio logistico e cose che non sono incluse</b></h2></p>
        <hr style="height: 5px; background-color: #3498db;">"""
    return text

def html_donation_text(lang='en'):
    text = ''
    if lang == 'en':
        text = """ <center><h2>Donation welcome!</h2></center> <br> 
        <p style="font-family:'Courier New'; font-size:20px;"> 
        <br>
        For <i>Bizum</1> use this number: <br>
        (+34) 686269566 <br>
        <br>
        For <i>Euro</i> transfer use this account number: <br> 
        ES37 0073 0100 5704 6207 6121 <br>
        Payable to: Genoveva Gonzalez Mirelis<br>
        <br>
        For <i>Vipps</i> use this number: <br> 
        (+47) 47669874 <br>
        <br>
        For <i>Kroner</i> transfer use this account number: <br> 
        NO93 6031 1712 228 <br>
        Payable to: Genoveva Gonzalez Mirelis<br>
        <br>
        </p>"""
    if lang == 'es':
        text = """ <center><h2>Se admiten donativos!</h2></center> <br> 
        <p style="font-family:'Courier New'; font-size:20px;"> 
        <br>
        Para hacer un <i>Bizum</1> usa este número: <br>
        (+34) 686269566 <br>
        <br>
        Para hacer una transferencia en <i>Euro</i> usa este número de cuenta: <br> 
        ES37 0073 0100 5704 6207 6121 <br>
        A nombre de: Genoveva González Mirelis<br>
        <br>
        Para hacer un <i>Vipps</i> usa este número: <br> 
        (+47) 47669874 <br>
        <br>
        Para hacer una transferencia en <i>Corona noruegas</i> usa este número de cuenta: <br> 
        NO93 6031 1712 228 <br>
        A nombre de: Genoveva González Mirelis<br>
        <br>
        </p>"""
    if lang == 'it':
        text = """ <center><h2>Donazioni sono le benvenute!</h2></center> <br> 
        <p style="font-family:'Courier New'; font-size:20px;"> 
        <br>
        Per <i>Bizum</1> usa questo numero: <br>
        (+34) 686269566 <br>
        <br>
        Per trasferimenti in <i>Euro</i> usa questo numero di conto: <br> 
        ES37 0073 0100 5704 6207 6121  <br>
        Intestato a: Genoveva Gonzalez Mirelis<br>
        <br>
        Per <i>Vipps</i> usa questo numero: <br> 
        (+47) 47669874 <br>
        <br>
        Per trasferimenti in <i>Corone Norvegesi</i> usa questo numero di conto: <br> 
        NO93 6031 1712 228 <br>
        Intestato a: Genoveva Gonzalez Mirelis<br>
        <br>
        </p>"""
    return text

def change_widget_labels_text(lang='en'):
    widget_labels = {}
    if lang == 'en':
        widget_labels['name_label'] = 'Name'
        widget_labels['surname_label'] = "Last Name"
        widget_labels['age_options_label'] = "Age Group"
        widget_labels['cerimony'] = "Yes, I will attend the ceremony at the District Board"
        widget_labels['banquet'] = "Yes, of course I will attend the banquet! What a question!"
        widget_labels['food_restrictions'] = "Yes, I have dietary restrictions"
        widget_labels['food_restrictions_details_label'] = "Dietary Restrictions"
        widget_labels['allergy'] = "Yes, I have some food allergies or intolerances"
        widget_labels['allergy_details_label'] = "Allergies or Intolerance"
        widget_labels['party'] = "Yes, I will go to the after party. Let's give it our all! *"
        widget_labels['lunch'] = "Yes, I'm up for lunch on Friday the 14th" # (on my own, at a restaurant yet to be decided)
        widget_labels['dinner'] = "Yes, I'm up for dinner on Friday the 14th" # (on my own, at a restaurant yet to be decided)
        widget_labels['hotel'] = "Yes, I would like you to help me book a hotel near Massi and Geno's house"
        widget_labels['room_label'] = "Room Type"
        widget_labels['date_range_picker_label'] = "Arrival and Departure Date"
        widget_labels['number_guest_label'] = "Number of Guests"
        # widget_labels['foot_note_1_description'] = """<p style="font-family:'Courier New'; font-size:15px;"><b><font color='orange'>*: Attention! Capacity is limited! <br> We greatly appreciate if you prioritize those coming from outside Madrid :-)</b>"""
        widget_labels['foot_note_2_description'] = """<p style="font-family:'Courier New'; font-size:15px;"><b><font color='orange'>*: Attention! By this time, the little ones should already be in bed, <br> so only adults can attend this part of the event!</b>"""
        widget_labels['foot_note_3_description'] = """<p style="font-family:'Courier New'; font-size:15px;"><b><font color='orange'>**: On my own, at a restaurant yet to be decided!</b>"""
        retiro_description_pane, restaurant_description_pane, casa_sposi_description_pane, black_jack_description_pane, pit_stop_description_pane = location_description(lang='en')
        widget_labels['retiro_description_pane'] = retiro_description_pane
        widget_labels['restaurant_description_pane'] = restaurant_description_pane
        widget_labels['casa_sposi_description_pane'] = casa_sposi_description_pane
        widget_labels['black_jack_description_pane'] = black_jack_description_pane
        widget_labels['pit_stop_description_pane'] = pit_stop_description_pane
        widget_labels['add_row'] = 'Add New Record'
        widget_labels['remove_row'] = 'Remove Selected Record'
        widget_labels['show_details'] = 'Show Table Details'
        widget_labels['submit_button'] = 'Submit Table'
        widget_labels['fetch_data_button'] = 'Check Your Data'
        widget_labels['modal_0_content'] = """<p style="font-family:'Courier New';"><b>Sorry, Can't add a record. Please check that you have provided an answer for the mandatory fields! <br> ['Name', 'Surname']</b></p>"""
        widget_labels['modal_1_content'] = """<p style="font-family:'Courier New';"><b>Can't submit empty Table! First add some records, and do not forget to fill the mandatory fields! <br> ['Name', 'Surname']</b></p>"""
        widget_labels['modal_2_content'] = """<p style="font-family:'Courier New';"><b>Record inserted successfully!</b></p>"""
        widget_labels['modal_3_content'] = """<p style="font-family:'Courier New';"><b>Congratulations all records have been successfully submitted!</b></p>"""
        widget_labels['modal_4_content'] = """<p style="font-family:'Courier New';"><b>Selection is empy, no records removed. Make sure to select one or more records from the Table.</b></p>"""


    if lang == 'it':
        widget_labels['name_label'] = 'Nome'
        widget_labels['surname_label'] = "Cognome"
        widget_labels['age_options_label'] = "Gruppo di età"
        widget_labels['cerimony'] = "Sì, parteciperò alla cerimonia presso la Giunta Distrettuale"
        widget_labels['banquet'] = "Sì, naturalmente parteciperò al banchetto! Che domanda!"
        widget_labels['food_restrictions'] = "Sì, ho restrizioni alimentari"
        widget_labels['food_restrictions_details_label'] = "Restrizioni Alimentari"
        widget_labels['allergy'] = "Sì, ho qualche allergia o intolleranza alimentare"
        widget_labels['allergy_details_label'] = "Allergie o Intolleranze"
        widget_labels['party'] = "Sì, parteciperò alla festa post-matrimonio. Diamo il massimo! *"
        widget_labels['lunch'] = "Sì, sono disponibile per pranzo venerdì 14" # (da solo, in un ristorante ancora da decidere)
        widget_labels['dinner'] = "Sì, sono disponibile per cena venerdì 14" # (da solo, in un ristorante ancora da decidere)
        widget_labels['hotel'] = "Sì, mi piacerebbe che mi aiutassi a prenotare un hotel vicino alla casa di Massi e Geno"
        widget_labels['room_label'] = "Tipo di Camera"
        widget_labels['date_range_picker_label'] = "Data di Arrivo e Partenza"
        widget_labels['number_guest_label'] = "Numero di Ospiti"
        #widget_labels['foot_note_1_description'] = """<p style="font-family:'Courier New'; font-size:15px;"><b><font color='orange'>*: Attenzione! La capacità è limitata! <br> Apprezziamo molto se dai priorità a chi viene da fuori Madrid :-)</b>"""
        widget_labels['foot_note_2_description'] = """<p style="font-family:'Courier New'; font-size:15px;"><b><font color='orange'>*: Attenzione! A quest'ora i più piccoli dovrebbero già essere a letto, <br> quindi solo gli adulti possono partecipare a questa parte dell'evento!</b>"""
        widget_labels['foot_note_3_description'] = """<p style="font-family:'Courier New'; font-size:15px;"><b><font color='orange'>**: Da solo, in un ristorante ancora da decidere!</b>"""
        retiro_description_pane, restaurant_description_pane, casa_sposi_description_pane, black_jack_description_pane, pit_stop_description_pane = location_description(lang='it')
        widget_labels['retiro_description_pane'] = retiro_description_pane
        widget_labels['restaurant_description_pane'] = restaurant_description_pane
        widget_labels['casa_sposi_description_pane'] = casa_sposi_description_pane
        widget_labels['black_jack_description_pane'] = black_jack_description_pane
        widget_labels['pit_stop_description_pane'] = pit_stop_description_pane
        widget_labels['add_row'] = 'Aggiungi Nuova Riga'
        widget_labels['remove_row'] = 'Rimuovi Righe Selezionate'
        widget_labels['show_details'] = 'Visualizza Dettgli Tabella'
        widget_labels['submit_button'] = 'Invia Tabella'
        widget_labels['fetch_data_button'] = 'Controlla i tuoi Dati'
        widget_labels['modal_0_content'] = "Scusa, non posso aggiungere un record. Controlla di aver fornito una risposta per i campi obbligatori! <br> ['Nome', 'Cognome']"
        widget_labels['modal_1_content'] = "Scusa, non posso inviare una tabella vuota! Prima aggiungi alcuni record, e non dimenticare di compilare i campi obbligatori! <br> ['Nome', 'Cognome']"
        widget_labels['modal_2_content'] = "Record inserito con successo!"
        widget_labels['modal_3_content'] = "Congratulazioni tutti i record sono stati inviati con successo!"
        widget_labels['modal_4_content'] = """<p style="font-family:'Courier New';"><b>La Selezione è vuota, nessun record rimosso. Assicurati di selezionare uno o più record dalla tabella.</b></p>"""
         

    if lang == 'es':
        widget_labels['name_label'] = 'Nombre'
        widget_labels['surname_label'] = "Apellidos"
        widget_labels['age_options_label'] = "Clase de edad"
        widget_labels['cerimony'] = "Sí, asistiré a la ceremonia en la Junta de Distrito"
        widget_labels['banquet'] = "Sí, por supuesto que asistiré al banquete! Qué pregunta!"
        widget_labels['food_restrictions'] = "Sí, tengo restricciones alimentarias"
        widget_labels['food_restrictions_details_label'] = "Restricciones alimentarias"
        widget_labels['allergy'] = "Sí, tengo alguna alergia o intolerancia alimentaria"
        widget_labels['allergy_details_label'] = "Alergias o intolerancia"
        widget_labels['party'] = "Sí, iré a la fiesta post-boda. A darlo todo! *"
        widget_labels['lunch'] = "Sí, me apunto a una comida el viernes 14" # (por cuenta propia, en un restaurante aún por decidir)
        widget_labels['dinner'] = "Sí, me apunto a una cena el viernes 14" # (por cuenta propia, en un restaurante aún por decidir)
        widget_labels['hotel'] = "Sí, me gustaría que me ayudaras a reservar hotel cerca de la casa de Massi y Geno"
        widget_labels['room_label'] = "Tipo de habitación"
        widget_labels['date_range_picker_label'] = "Dia de llegada y partida"
        widget_labels['number_guest_label'] = "Número de huéspedes"
        #widget_labels['foot_note_1_description'] = """<p style="font-family:'Courier New'; font-size:15px;"> <b><font color='orange'>*: Atención! El aforo es limitado! <br> Os agradecemos infinito si le dáis prioridad a los que vienen de fuera de Madrid :-)</b></p>"""
        widget_labels['foot_note_2_description'] = """<p style="font-family:'Courier New'; font-size:15px;"> <b><font color='orange'>*: Atención! A estas horas los peques ya tienen que estar en la cama, <br> así que a esta parte del evento solo podrán asistir los mayores!</b>"""
        widget_labels['foot_note_3_description'] = """<p style="font-family:'Courier New'; font-size:15px;"><b><font color='orange'>**: Por cuenta propia, en un restaurante aún por decidir!</b>"""
        retiro_description_pane, restaurant_description_pane, casa_sposi_description_pane, black_jack_description_pane, pit_stop_description_pane = location_description(lang='es')
        widget_labels['retiro_description_pane'] = retiro_description_pane
        widget_labels['restaurant_description_pane'] = restaurant_description_pane
        widget_labels['casa_sposi_description_pane'] = casa_sposi_description_pane
        widget_labels['black_jack_description_pane'] = black_jack_description_pane
        widget_labels['pit_stop_description_pane'] = pit_stop_description_pane
        widget_labels['add_row'] = 'Agregar nueva línea'
        widget_labels['remove_row'] = 'Eliminar línea seleccionada'
        widget_labels['show_details'] = 'Mostrar detalles de la tabla'
        widget_labels['submit_button'] = 'Enviar tabla'
        widget_labels['fetch_data_button'] = 'Comprueba tus datos'
        widget_labels['modal_0_content'] = "Lo siento, no puedo agregar un registro. ¡Por favor, verifica que has proporcionado una respuesta para los campos obligatorios! <br> ['Nombre', 'Apellidos']"
        widget_labels['modal_1_content'] = "¡No puedo enviar una tabla vacía! ¡Primero agrega algunos registros, y no olvides completar los campos obligatorios! <br> ['Nombre', 'Apellidos']"
        widget_labels['modal_2_content'] = "¡Registro insertado con éxito!"
        widget_labels['modal_3_content'] = "¡Felicidades todos los registros se han enviado con éxito!"
        widget_labels['modal_4_content'] = """<p style="font-family:'Courier New';"><b>La Selección está vacía, no se eliminaron registros. Asegúrate de seleccionar uno o más registros de la tabla.</b></p>"""    
    return widget_labels
