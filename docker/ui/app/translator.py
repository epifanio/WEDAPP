from wed_map import location_description

def intro_text(lang='en'):
    if lang == 'en':
        text = """ <h1> We're Getting Married, and We Want to Celebrate WITH YOU </h1> <br>
        <br>
        <p style="font-family:'Courier New'; font-size:20px;"> Here are the most important details:<br>
        <br>
        A simple ceremony will take place at the Retiro District Municipal Board at 11:00 a.m.<br>
        <br>
        This will be followed by a grand banquet at the fabulous Seeds Restaurant, starting at 2:00 p.m., where<br>
        we'll spend the entire afternoon among friends, music, refreshments, and a few surprises.<br>
        <br>
        And for those with more stamina, we'll see you at the post-wedding party at Black Jack club<br>
        (better known to our close friends as the Cat's Temple) starting at 10:00 p.m.!
        <br>
        All this and much more, on <b>June 15, 2024</b>.<br>
        <br>
        We've created this app for you to confirm your attendance, as well as to provide us with any information we need to make everything perfect on that day,<br>
        also for you!<br>
        <br>
        We eagerly await your response,<br>
        <br>
        Massi & Geno<br>
        <br>
        <br></p>
        P.S.: Please send us your form responses before June 1st!"""
    if lang == 'es':
        text = """ <h1> Nos casamos, y queremos celebrarlo CONTIGO </h1> <br>
        <br>
        <p style="font-family:'Courier New'; font-size:20px;"> Estos son los datos más importantes:<br>
        <br>
        Una sencilla ceremonia tendrá lugar en la Junta Municipal de Distrito de Retiro a las 11:00.<br>
        <br>
        Le seguirá un gran banquete en el fabuloso Restaurante Seeds, a partir de las 14:00, y donde <br>
        pasaremos toda la tarde entre amigos, música, refrigerios, y alguna que otra sorpresa.<br>
        <br>
        Y a los que tengáis más aguante, os vemos en la fiesta post-boda en el club Black Jack<br>
        (más conocido para los allegados como el Templo del Gato) a partir de las 22:00!<br>
        <br>
        Todo esto y mucho más, el <b>15 de junio de 2024</b>.<br>
        <br>
        Hemos creado esta applicación para que nos puedas confirmar tu asistencia, así como para <br>
        trasladarnos toda la información que nos hacen falta para que todo sea perfecto ese día, <br>
        también para tí!<br>
        <br>
        Os esperamos ansiosos,<br>
        <br>
        Massi & Geno<br>
        <br>
        <br></p>
        PD: Por favor, mandadnos las respuestas del formulario antes del 1 de junio!"""
    if lang == 'it':
        text = """ <h1> Ci sposiamo e vogliamo festeggiare CON TE </h1> <br>
        <br>
        <p style="font-family:'Courier New'; font-size:20px;"> Ecco i dettagli più importanti:<br>
        <br>
        Una semplice cerimonia avrà luogo presso il Municipio del Distretto di Retiro alle 11:00.<br>
        <br>
        Seguirà un grande banchetto nel favoloso Ristorante Seeds, a partire dalle 14:00, dove<br>
        trascorreremo tutto il pomeriggio tra amici, musica, rinfreschi e qualche sorpresa.<br>
        <br>
        E per coloro che hanno più resistenza, ci vediamo alla festa post-matrimonio nel club Black Jack<br>
        (meglio conosciuto tra gli amici come il Tempio del Gatto) a partire dalle 22:00!
        <br>
        Tutto questo e molto altro, il <b>15 giugno 2024</b>.<br>
        <br>
        Abbiamo creato questa app per permetterti di confermare la tua presenza, e anche per fornirci tutte le informazioni necessarie per rendere perfetto quel giorno,<br>
        anche per te!<br>
        <br>
        Attendiamo con ansia la tua risposta,<br>
        <br>
        Massi & Geno<br>
        <br>
        <br></p>
        P.S.: Ti preghiamo di inviarci le risposte al modulo prima del 1° giugno!"""
    return text

def default_separator_text(lang='en'):
    if lang == 'en':
        text = """ <p><h2><b> The Wedding Bash: What It Includes </b></h2></p>
        <br>
        <hr style="height: 5px; background-color: #3498db;">
        <br>
        Remember to add the details of all your companions, as well as your own, one by one."""
    if lang == 'es':
        text = """ <p><h2><b> El bodorrio: todo lo que incluye </b></h2></p>
        <br>
        <hr style="height: 5px; background-color: #3498db;">
        <br> 
        Acuérdate de agregar los datos de todos tus acompañantes, así como los tuyos propios, de uno en uno"""
    if lang == 'it':
        text = """<p><h2><b> Il Matrimonio: Tutto ciò che Include </b></h2></p>
        <br>
        <hr style="height: 5px; background-color: #3498db;">
        <br> 
        Ricorda di aggiungere i dati di tutti i tuoi accompagnatori, così come i tuoi, uno per uno. """
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

def html_donation_text(lang='en'):
    text = ''
    if lang == 'en':
        text = """ <h2>Bank details:</h2> <br> 
        <p style="font-family:'Courier New'; font-size:20px;"> 
        Donation welcome!!! <br>
        For <i>Bizum</1> use this number: <br>
        (+34) 686269566 <br>
        <br>
        For <i>Euro</i> transfer use this account number: <br> 
        ES37 0073 0100 5704 6207 6121 <br>
        <br>
        For <i>Vipps</i> use this number: <br> 
        (+47) 47669874 <br>
        <br>
        For <i>Kroner</i> transfer use this account number: <br> 
        NO93 6031 1712 228 <br>
        <br>
        </p>"""
    if lang == 'es':
        text = """ <h2>Bank details:</h2> <br> 
        <p style="font-family:'Courier New'; font-size:20px;"> 
        Se admiten donativos!!! <br>
        Para hacer un <i>Bizum</1> usa este número: <br>
        (+34) 686269566 <br>
        <br>
        Para hacer una transferencia en <i>Euro</i> usa este número de cuenta: <br> 
        ES37 0073 0100 5704 6207 6121 <br>
        <br>
        Para hacer un <i>Vipps</i> usa este número: <br> 
        (+47) 47669874 <br>
        <br>
        Para hacer una transferencia en <i>Corona noruegas</i> usa este número de cuenta: <br> 
        NO93 6031 1712 228 <br>
        <br>
        </p>"""
    if lang == 'it':
        text = """ <h2>Bank details:</h2> <br> 
        <p style="font-family:'Courier New'; font-size:20px;"> 
        Donazioni sono ben accette :) !!! <br>
        Per <i>Bizum</1> usa questo numero: <br>
        (+34) 686269566 <br>
        <br>
        Per trasferimenti in <i>Euro</i> usa questo numero di conto: <br> 
        ES37 0073 0100 5704 6207 6121  <br>
        <br>
        Per <i>Vipps</i> usa questo numero: <br> 
        (+47) 47669874 <br>
        <br>
        Per trasferimenti in <i>Corone Norvegesi</i> usa questo numero di conto: <br> 
        NO93 6031 1712 228 <br>
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
        widget_labels['party'] = "Yes, I will go to the post-wedding party. Let's give it our all!"
        widget_labels['lunch'] = "Yes, I'm up for lunch on Friday the 14th" # (on my own, at a restaurant yet to be decided)
        widget_labels['dinner'] = "Yes, I'm up for dinner on Friday the 14th" # (on my own, at a restaurant yet to be decided)
        widget_labels['hotel'] = "Yes, I would like you to help me book a hotel near Massi and Geno's house"
        widget_labels['room_label'] = "Room Type"
        widget_labels['date_range_picker_label'] = "Arrival and Departure Date"
        widget_labels['number_guest_label'] = "Number of Guests"
        widget_labels['foot_note_1_description'] = "<b><font color='red'>*: Attention! Capacity is limited! We greatly appreciate if you prioritize those coming from outside Madrid :-)</b>"
        widget_labels['foot_note_2_description'] = "<b><font color='red'>**: Attention! By this time, the little ones should already be in bed, so only adults can attend this part of the event!</b>"
        widget_labels['foot_note_3_description'] = "<b><font color='red'>***: On my own, at a restaurant yet to be decided!</b>"
        retiro_description_pane, restaurant_description_pane, casa_sposi_description_pane, black_jack_description_pane = location_description(lang='en')
        widget_labels['retiro_description_pane'] = retiro_description_pane
        widget_labels['restaurant_description_pane'] = restaurant_description_pane
        widget_labels['casa_sposi_description_pane'] = casa_sposi_description_pane
        widget_labels['black_jack_description_pane'] = black_jack_description_pane

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
        widget_labels['party'] = "Sì, parteciperò alla festa post-matrimonio. Diamo il massimo!"
        widget_labels['lunch'] = "Sì, sono disponibile per pranzo venerdì 14" # (da solo, in un ristorante ancora da decidere)
        widget_labels['dinner'] = "Sì, sono disponibile per cena venerdì 14" # (da solo, in un ristorante ancora da decidere)
        widget_labels['hotel'] = "Sì, mi piacerebbe che mi aiutassi a prenotare un hotel vicino alla casa di Massi e Geno"
        widget_labels['room_label'] = "Tipo di Camera"
        widget_labels['date_range_picker_label'] = "Data di Arrivo e Partenza"
        widget_labels['number_guest_label'] = "Numero di Ospiti"
        widget_labels['foot_note_1_description'] = "<b><font color='red'>*: Attenzione! La capacità è limitata! Apprezziamo molto se dai priorità a chi viene da fuori Madrid :-)</b>"
        widget_labels['foot_note_2_description'] = "<b><font color='red'>**: Attenzione! A quest'ora i più piccoli dovrebbero già essere a letto, quindi solo gli adulti possono partecipare a questa parte dell'evento!</b>"
        widget_labels['foot_note_3_description'] = "<b><font color='red'>***: Da solo, in un ristorante ancora da decidere!</b>"
        retiro_description_pane, restaurant_description_pane, casa_sposi_description_pane, black_jack_description_pane = location_description(lang='it')
        widget_labels['retiro_description_pane'] = retiro_description_pane
        widget_labels['restaurant_description_pane'] = restaurant_description_pane
        widget_labels['casa_sposi_description_pane'] = casa_sposi_description_pane
        widget_labels['black_jack_description_pane'] = black_jack_description_pane
        

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
        widget_labels['party'] = "Sí, iré a la fiesta post-boda. A darlo todo!"
        widget_labels['lunch'] = "Sí, me apunto a una comida el viernes 14" # (por cuenta propia, en un restaurante aún por decidir)
        widget_labels['dinner'] = "Sí, me apunto a una cena el viernes 14" # (por cuenta propia, en un restaurante aún por decidir)
        widget_labels['hotel'] = "Sí, me gustaría que me ayudaras a reservar hotel cerca de la casa de Massi y Geno"
        widget_labels['room_label'] = "Tipo de habitación"
        widget_labels['date_range_picker_label'] = "Dia de llegada y partida"
        widget_labels['number_guest_label'] = "Número de huéspedes"
        widget_labels['foot_note_1_description'] = "<b><font color='red'>*: Atención! El aforo es limitado! Os agradecemos infinito si le dáis prioridad a los que vienen de fuera de Madrid :-)</b>"
        widget_labels['foot_note_2_description'] = "<b><font color='red'>**: Atención! A estas horas los peques ya tienen que estar en la cama, así que a esta parte del evento solo podrán asistir los mayores!</b>"
        widget_labels['foot_note_3_description'] = "<b><font color='red'>***: Por cuenta propia, en un restaurante aún por decidir!</b>"
        retiro_description_pane, restaurant_description_pane, casa_sposi_description_pane, black_jack_description_pane = location_description(lang='es')
        widget_labels['retiro_description_pane'] = retiro_description_pane
        widget_labels['restaurant_description_pane'] = restaurant_description_pane
        widget_labels['casa_sposi_description_pane'] = casa_sposi_description_pane
        widget_labels['black_jack_description_pane'] = black_jack_description_pane
    return widget_labels
