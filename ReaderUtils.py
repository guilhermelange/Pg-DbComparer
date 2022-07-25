from Connection import Connection

def return_select_array(data):
    try:
        return [item[0] for item in data]
    except:
        return []

def return_column_map(data):
    result = {}
    for item in data:
        table_name = item[0]
        column_name = item[1]
        is_nullable = item[2]
        data_type = item[3]

        if not(table_name in result):
            result[table_name] = []

        result[table_name].append({'table_name': table_name, 'column_name': column_name, 'is_nullable': is_nullable, 'data_type' : data_type})

    return result

def getData(database):
    con = Connection(database.host, database.port, database.db, database.user, database.password)
    sql = """
        SELECT table_name 
        FROM information_schema.tables t 
        WHERE table_schema = 'public' 
        AND table_type = 'BASE TABLE' 
        AND table_catalog = '{0}'
    """

    rs = con.query(sql.format(database.db))
    table = return_select_array(rs)

    sql = """
        SELECT sequence_name 
        FROM information_schema.sequences s 
        WHERE sequence_schema = 'public' 
        AND sequence_catalog = '{0}'
    """
    rs = con.query(sql.format(database.db))
    sequence = return_select_array(rs)

    sql = """
        SELECT c.table_name, c.column_name, c.is_nullable, c.data_type 
        FROM information_schema.columns c 
            JOIN information_schema.tables t ON c.table_catalog = t.table_catalog AND c.table_name = t.table_name 
        WHERE c.table_catalog = '{0}'
        AND c.table_schema = 'public'
        AND t.table_type = 'BASE TABLE'
        ORDER BY table_name
    """
    rs = con.query(sql.format(database.db))
    columns = return_column_map(rs)

    return table, sequence, columns



