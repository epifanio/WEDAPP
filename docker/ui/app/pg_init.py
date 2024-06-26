import psycopg2
import pandas as pd

def init_pg_db(table):
    # Load your DataFrame (replace this with your actual DataFrame)
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
            'Session' : [],
            'User_id': [],
    }, index=[])


    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname='mydatabase',
        user='myuser',
        password='mypassword',
        host='db'
    )

    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    # Define the table schema
    table_schema = f"""
        CREATE TABLE IF NOT EXISTS {table} (
            id SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Surname VARCHAR(100),
            Age VARCHAR(100),
            Cerimony BOOLEAN,
            Banquet BOOLEAN,
            Food_restrictions BOOLEAN,
            Food_restrictions_details VARCHAR(255),
            Allergy BOOLEAN,
            Allergy_details VARCHAR(255),
            Party BOOLEAN,
            Friday_lunch BOOLEAN,
            Friday_dinner BOOLEAN,
            Hotel BOOLEAN,
            Room_details VARCHAR(255),
            Days VARCHAR(100),
            Guest INTEGER,
            Session timestamp,
            User_id VARCHAR(100)
        )
    """

    # Execute the schema creation
    cursor.execute(table_schema)

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

