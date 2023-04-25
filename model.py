"""Model Module for Translation Management App"""

import sqlite3


class Model:
    """This Class handles the interaction ith database and all database logic"""

    TABLE_NAME = 'translatio'

    TABLE_SCHEMA = [
        {'col_name': 'RID', 'data_type': 'INTEGER PRIMARY KEY AUTOINCREMENT'},
        {'col_name': 'description', 'data_type': 'TEXT'},
        {'col_name': 'subject', 'data_type': 'TEXT'},
        {'col_name': 'source_lang', 'data_type': 'TEXT'},
        {'col_name': 'target_lang', 'data_type': 'TEXT'},
        {'col_name': 'year', 'data_type': 'INT'},
        {'col_name': 'month', 'data_type': 'INT'},
        {'col_name': 'client', 'data_type': 'TEXT'},
        {'col_name': 'source_path', 'data_type': 'TEXT'},
        {'col_name': 'target_path', 'data_type': 'TEXT'},
        {'col_name': 'quantity', 'data_type': 'INT'},
        {'col_name': 'unit', 'data_type': 'TEXT'},
        {'col_name': 'is_deleted', 'data_type': 'INT'}
    ]

    def __init__(self):
        self.connection = sqlite3.connect('translations.db')
        self._create_connect_table(self.connection, self.TABLE_NAME, self.TABLE_SCHEMA)

    @staticmethod
    def _create_connect_table(conn, table_name, schema):
        # Construct Query to Connect to the Table
        CREATE_CONNECT_TRANS_TABLE_QUERY = f"CREATE TABLE IF NOT EXISTS {table_name}("
        for column in schema:
            CREATE_CONNECT_TRANS_TABLE_QUERY += f'{column["col_name"]} {column["data_type"]}, '
        CREATE_CONNECT_TRANS_TABLE_QUERY = CREATE_CONNECT_TRANS_TABLE_QUERY[:-2] + ')'

        # Execute SQL command to connect to the table
        with conn:
            conn.execute(CREATE_CONNECT_TRANS_TABLE_QUERY)

    def add_record_to_table(self, conn, data: list[dict]):
        # Construct the Add Record Query
        ADD_RECORD_QUERY = f"INSERT INTO {self.TABLE_NAME} ("
        ADD_RECORD_QUERY += ", ".join(k['col_name'] for k in self.TABLE_SCHEMA[1:])
        ADD_RECORD_QUERY += ') VALUES ('
        ADD_RECORD_QUERY += ", ".join('?' for i in range(len(self.TABLE_SCHEMA) - 2))
        ADD_RECORD_QUERY += ", 0)"

        # Construct the parameters string
        params = tuple([list(d.values())[0] for d in data])

        # Execute SQL command to add a new record with given data
        with conn:
            conn.execute(ADD_RECORD_QUERY, params)

    def get_all_records(self, table_name):
        pass

# x = Model()
# d = [
#     {'description': "sacrifice"}, {'subject': "liefervertrag"}, {"source_lang": "EN"}, {"target_lang": "DE"},
#     {"year": 554},  {"month": 12}, {"client": ""}, {"source_path": ""}, {"target_path": ""}, {"quantity": 45},
#     {"unit": "words"}
#      ]
# x.add_record_to_table(x.connection, d)


