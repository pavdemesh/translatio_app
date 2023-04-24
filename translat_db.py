import sqlite3

CREATE_TRANS_TABLE = """CREATE TABLE IF NOT EXISTS translatio(
            year INT, month INT, description TEXT,
            target_path TEXT, source_path TEXT,
            target_lang TEXT, source_lang TEXT,
            subject TEXT, client TEXT, quantity INT, unit INT)"""

INSERT_TRANS = "INSERT INTO translatio VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

GET_ALL_TRANS = "SELECT * FROM translatio"

GET_TRANS_BY_CLIENT = "SELECT rowid, * FROM translatio WHERE client = ?"

UPDATE_CLIENT_BY_ID = "UPDATE translatio SET client = ? where rowid = ?"


# create new or connect to existing database for translations
def connect_db():
    return sqlite3.connect('translations.db')

def create_connect_table(conn):
    with conn:
        conn.execute(CREATE_TRANS_TABLE)


def add_translation(connection, year=0, month=0, description='n/a', target_path='n/a', source_path='n/a', 
                    target_lang='n/a', source_lang='n/a', subject='n/a', client='n/a', quantity=0, unit=0):
    with connection:
        connection.execute(INSERT_TRANS, (year, month, description, target_path, source_path, target_lang, source_lang, subject, client, quantity, unit))


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
