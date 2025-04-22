import psycopg2
import configparser

def load_config(filename='database.ini', section='postgresql'):
    parser = configparser.ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    return db

def connect(config):
    try:
        conn = psycopg2.connect(**config)
        return conn
    except psycopg2.DatabaseError as error:
        print(f"Database error: {error}")

