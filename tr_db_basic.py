import sqlite3

CREATE_TRANS_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS translatio(
            description TEXT, subject TEXT, source_lang TEXT, target_lang TEXT,
            year INT, month INT, client TEXT, 
            source_path TEXT, target_path TEXT, quantity INT, unit TEXT, is_deleted INT,)"""

INSERT_TRANS_QUERY = """INSERT INTO translatio 
                (description, subject, source_lang, target_lang, year, month, client,
                source_path, target_path, quantity, unit, is_deleted)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0)"""

GET_ALL_TRANS = "SELECT * FROM translatio"

GET_TRANS_BY_CLIENT = "SELECT rowid, * FROM translatio WHERE client = ?"

UPDATE_CLIENT_BY_ID = "UPDATE translatio SET client = ? where rowid = ?"


# create new or connect to existing database for translations
def connect_db():
    return sqlite3.connect('translations.db')


def create_connect_table(conn):
    with conn:
        conn.execute(CREATE_TRANS_TABLE_QUERY)


def add_translation(connection, description='n/a', subject='n/a', source_lang='n/a', target_lang='n/a',
                    year=0, month=0, client='n/a',
                    source_path='n/a', target_path='n/a', quantity=0, unit='n/a'):
    insert_params = (description, subject, source_lang, target_lang, year, month, client, source_path, target_path,
                     quantity, unit)
    with connection:
        connection.execute(INSERT_TRANS_QUERY, insert_params)


def get_all_trans(connection):
    with connection:
        for row in connection.execute(GET_ALL_TRANS).fetchall():
            print(row)


def get_trans_by_client(connection, client):
    with connection:
        for row in connection.execute(GET_TRANS_BY_CLIENT, (client,)).fetchall():
            print(row)


def update_tr_client_by_id(connection, client, rid):
    with connection:
        connection.execute(UPDATE_CLIENT_BY_ID, (client, rid))
