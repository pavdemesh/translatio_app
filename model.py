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
        self._create_connect_table()

    def _create_connect_table(self):
        # Construct Query to Connect to the Table
        CREATE_CONNECT_TRANS_TABLE_QUERY = f"CREATE TABLE IF NOT EXISTS {self.TABLE_NAME}("
        # Add Column names and data types to the query text
        for column in self.TABLE_SCHEMA:
            CREATE_CONNECT_TRANS_TABLE_QUERY += f'{column["col_name"]} {column["data_type"]}, '
        # Finalize query text - remove redundant ', '
        CREATE_CONNECT_TRANS_TABLE_QUERY = CREATE_CONNECT_TRANS_TABLE_QUERY[:-2] + ')'

        # Execute SQL command to connect to the table and execute the query
        with self.connection:
            self.connection.execute(CREATE_CONNECT_TRANS_TABLE_QUERY)

    def add_record_to_table(self, params: tuple):
        # Construct the Add Record Query
        # Generate starting part of the query
        ADD_RECORD_QUERY = f"INSERT INTO {self.TABLE_NAME} ("
        # Add cColumn names from schema except the first column (ID)
        ADD_RECORD_QUERY += ", ".join(k['col_name'] for k in self.TABLE_SCHEMA[1:])
        # Continue the Query Formation
        ADD_RECORD_QUERY += ') VALUES ('
        # Add placeholder "?" equal to   number of columns minus 2 (
        ADD_RECORD_QUERY += ", ".join('?' for i in range(len(self.TABLE_SCHEMA) - 2))
        # Add 0 (default value) for is_deleted column
        ADD_RECORD_QUERY += ", 0)"

        # Execute SQL command: Query + params to insert data into table
        with self.connection:
            self.connection.execute(ADD_RECORD_QUERY, params)

    def deliver_all_visible_records(self) -> list[tuple]:
        GET_ALL_QUERY = f'SELECT * FROM {self.TABLE_NAME} WHERE is_deleted = 0'
        with self.connection:
            return self.connection.execute(GET_ALL_QUERY).fetchall()

    def deliver_all_present_records(self) -> list[tuple]:
        GET_ALL_QUERY = f'SELECT * FROM {self.TABLE_NAME}'
        with self.connection:
            return self.connection.execute(GET_ALL_QUERY).fetchall()

    def mark_one_record_deleted_by_id(self, row_id):
        with self.connection:
            RECORD_DELETION_QUERY = f"UPDATE {self.TABLE_NAME} SET is_deleted = 1 WHERE RID = ?"
            print(RECORD_DELETION_QUERY)
            self.connection.execute(RECORD_DELETION_QUERY, (row_id,))
#
# x = Model()
# data = ("TEST", "delete", "UA", "DE", 2022, 7, "", "", "", 1231, "hours")
# x.add_record_to_table(data)
# #
# x.mark_one_record_deleted_by_id(5)
