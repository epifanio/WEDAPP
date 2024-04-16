
from ipyleaflet import Map, Marker, Icon, Popup, LayersControl, FullScreenControl
from ipywidgets import HTML
import panel as pn
#pn.extension()

def getMap():
    # Create a Map
    m = Map(center=(40.43817, -3.68661), zoom=12)
    m.layout.width = '100%'
    # Define marker positions
    positions = [
        (40.41874, -3.70753),  # Party
        (40.43817, -3.68661),    # Ricevimento
        (40.40233, -3.67743),    # Cerimonia
        (40.4313, -3.67187)    # Casa Sposi
    ]
    
    # Define marker labels
    labels = ['A', 'B', 'C', 'D']
    
    # Define marker attributes

    gmap_retiro_url = "https://www.google.com/maps/place/Junta+Municipal+del+Distrito+de+Retiro/@40.4023436,-3.6800094,17z/data=!4m6!3m5!1s0xd422610b505fc9d:0x643675481cabd4b0!8m2!3d40.4023395!4d-3.6774345!16s%2Fg%2F11c2nw4xrl?entry=ttu"
    gmap_restaurant_url = "https://www.google.com/maps/place/Restaurante+Seeds/@40.4381732,-3.6866107,15z/data=!4m6!3m5!1s0xd42293d73d2c977:0x819dc39751a2d781!8m2!3d40.4381732!4d-3.6866107!16s%2Fg%2F11pd2xqyxl?entry=ttu"
    gmap_url_casa_sposi = "https://www.google.com/maps/place/C%2F+de+Francisco+Silvela,+27,+6+c,+Salamanca,+28028+Madrid/@40.4313076,-3.6744468,17z/data=!3m1!4b1!4m5!3m4!1s0xd4228b77a09fc2d:0x69b75571be49d39!8m2!3d40.4313035!4d-3.6718719?entry=ttu"
    gmap_url_black_jack = "https://www.google.com/maps/place/Black+Jack+Club/@40.4187465,-3.7101133,17z/data=!3m1!4b1!4m6!3m5!1s0xd4229d71079ac6d:0x1a27a5ce4dada59b!8m2!3d40.4187424!4d-3.7075384!16s%2Fg%2F11kqq9rdk9?entry=ttu"

    gmap_retiro = f"""<p style="font-family:'Courier New'; font-size:15px;"><a href="{gmap_retiro_url}" target="_blank"> Pl. de Daoíz y Velarde, 2, Retiro, 28007 Madrid </a></p>"""
    gmap_restaurant = f"""<p style="font-family:'Courier New'; font-size:15px;"><a href="{gmap_restaurant_url}" target="_blank"> C. de Serrano, 95, Chamartín, 28006 Madrid </a></p>"""
    gmap_casa_sposi = f"""<p style="font-family:'Courier New'; font-size:15px;"><a href="{gmap_url_casa_sposi}" target="_blank"> C. de Francisco Silvela, 27, 6 C, 28028 Madrid </a></p>"""
    gmap_black_jack = f"""<p style="font-family:'Courier New'; font-size:15px;"><a href="{gmap_url_black_jack}" target="_blank"> C. de Trujillos, 7, Centro, 28013 Madrid </a></p>"""

    # attributes = [
    #     {'name': 'Party', 'description': '<b>Party post boda </b> <br> <a href="https://www.venuesplace.com/es/11035-black-jack" target="_blank">Black Jack Club</a> <br> C. de Trujillos, 7, Centro, 28013 Madrid'},
    #     {'name': 'Ricevimento', 'description': '<b>Ricevimento </b> <br> <a href="http://www.restauranteseeds.com/" target="_blank">Restaurante Seeds</a> <br> C. de Serrano, 95, Chamartín, 28006 Madrid'},
    #     {'name': 'Cerimonia', 'description': '<b>Cerimonia </b> <br> Junta Municipal del Distrito de Retiro <br> Pl. de Daoíz y Velarde, 2, Retiro, 28007 Madrid'},
    #     {'name': 'Casa Sposi', 'description': '<b>Casa Sposi </b> <br> C/ de Francisco Silvela, 27, 6 C'}
    # ]

    
    attributes = [
        {"name": "Party", "description": f"<b> After Party </b> <br> {gmap_black_jack}"},
        {"name": "Ricevimento", "description": f"<b>Ricevimento </b> <br> {gmap_restaurant}"},
        {"name": "Cerimonia", "description": f"<b>Cerimonia </b> <br> {gmap_retiro}"},
        {"name": "Casa degli Sposi", "description": f"<b>Casa degli Sposi </b> <br>{gmap_casa_sposi}"}
    ]

    # Add markers with labels
    markers = []
    for i, (lat, lon) in enumerate(positions):
        marker = Marker(location=(lat, lon), draggable=False, name=attributes[i]['name'])
        marker.icon = Icon(icon_url='https://leafletjs.com/examples/custom-icons/leaf-red.png',
                           icon_size=[25, 41], icon_anchor=[12, 41],
                           html=f'<div style="font-size: 12pt; color: black;">{labels[i]}</div>')
        marker.attribute = attributes[i]  # Assign attributes to marker
        
        # marker.on_click(on_marker_click)  # Attach click event handler to marker
        message_marker = HTML()
        message_marker.value = attributes[i]['description']
        # message_marker.placeholder = attributes[i]['description']
        # message_marker.description = attributes[i]['name']
        marker.popup = message_marker
        markers.append(marker)
    for i in markers:    
        m.add_layer(i)
    
    control = LayersControl(position='topright')
    m.add(control)
    m.add(FullScreenControl())


    # Display the map and output widget
    return m #display(m)


def location_description(lang='en'):
    if lang == 'en':
        cerimony = "Ceremony"
        casa_sposi = "Bride and Groom's house"
        party_post_boda = "After Party"
        restaurant = "Restaurant"
    if lang == 'it':
        cerimony = "Cerimonia"
        casa_sposi = "Casa degli Sposi"
        party_post_boda = "Festa post-matrimonio"
        restaurant = "Ricevimento"
    if lang == 'es':
        cerimony = "Ceremonia"
        casa_sposi = "Casa de los novios"
        party_post_boda = "Fiesta post-boda"
        restaurant = "Restaurante"
    
    
    gmap_retiro_url = "https://www.google.com/maps/place/Junta+Municipal+del+Distrito+de+Retiro/@40.4023436,-3.6800094,17z/data=!4m6!3m5!1s0xd422610b505fc9d:0x643675481cabd4b0!8m2!3d40.4023395!4d-3.6774345!16s%2Fg%2F11c2nw4xrl?entry=ttu"
    gmap_restaurant_url = "https://www.google.com/maps/place/Restaurante+Seeds/@40.4381732,-3.6866107,15z/data=!4m6!3m5!1s0xd42293d73d2c977:0x819dc39751a2d781!8m2!3d40.4381732!4d-3.6866107!16s%2Fg%2F11pd2xqyxl?entry=ttu"
    gmap_url_casa_sposi = "https://www.google.com/maps/place/C%2F+de+Francisco+Silvela,+27,+6+c,+Salamanca,+28028+Madrid/@40.4313076,-3.6744468,17z/data=!3m1!4b1!4m5!3m4!1s0xd4228b77a09fc2d:0x69b75571be49d39!8m2!3d40.4313035!4d-3.6718719?entry=ttu"
    gmap_url_black_jack = "https://www.google.com/maps/place/Black+Jack+Club/@40.4187465,-3.7101133,17z/data=!3m1!4b1!4m6!3m5!1s0xd4229d71079ac6d:0x1a27a5ce4dada59b!8m2!3d40.4187424!4d-3.7075384!16s%2Fg%2F11kqq9rdk9?entry=ttu"

    gmap_retiro = f"""<p style="font-family:'Courier New'; font-size:15px;"><a href="{gmap_retiro_url}" target="_blank"> Pl. de Daoíz y Velarde, 2, Retiro, 28007 Madrid </a></p>"""
    gmap_restaurant = f"""<p style="font-family:'Courier New'; font-size:18px;"><a href="{gmap_restaurant_url}" target="_blank"> C. de Serrano, 95, Chamartín, 28006 Madrid </a></p>"""
    gmap_casa_sposi = f"""<p style="font-family:'Courier New'; font-size:18px;"><a href="{gmap_url_casa_sposi}" target="_blank"> C. de Francisco Silvela, 27, 6 C, 28028 Madrid </a></p>"""
    gmap_black_jack = f"""<p style="font-family:'Courier New'; font-size:18px;"><a href="{gmap_url_black_jack}" target="_blank"> C. de Trujillos, 7, Centro, 28013 Madrid </a></p>"""
    
    retiro_description = f"""<p style="font-family:'Courier New'; font-size:20px;"><b>{cerimony} </b></p>  {gmap_retiro}"""
    restaurant_description = f""" <p style="font-family:'Courier New'; font-size:20px;"><b>{restaurant}</b></p>  {gmap_restaurant}"""
    casa_sposi_description = f""" <p style="font-family:'Courier New'; font-size:20px;"><b>{casa_sposi}</b></p>  {gmap_casa_sposi}"""
    black_jack_description = f"""<p style="font-family:'Courier New'; font-size:20px;"><b>{party_post_boda}</b></p>  {gmap_black_jack}"""
    return retiro_description, restaurant_description, casa_sposi_description, black_jack_description
