import tr_db_basic as trdb

connection = trdb.connect_db()
trdb.create_connect_table(connection)

trdb.add_translation(connection)

trdb.update_tr_client_by_id(connection, 'Lisle', '2')
trdb.update_tr_client_by_id(connection, 'n/a', '3')
trdb.update_tr_client_by_id(connection, 'Lisle', '4')

# trdb.get_all_trans(connection)

# trdb.get_trans_by_client(connection, 'Lisle')
