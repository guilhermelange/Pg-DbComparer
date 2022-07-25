def format_table(create_tables, tables):
    sdt_create_table = ""
    for item in create_tables:
        current_table = tables.get(item)
        sql = '''CREATE TABLE {0} ({1});\n'''
        columnSql = ""
        for column in current_table:
            columnSql += "{0} {1}".format(column['column_name'], column['data_type'])

        sql = sql.format(item, columnSql)
        sdt_create_table += sql

    return sdt_create_table


def format_table_column(columns):
    sql_alter_table = ""

    for column in columns:
        sql = '''ALTER TABLE {0} ADD COLUMN {1} {2};\n'''
        sql = sql.format(column['table_name'], column['column_name'], column['data_type'])
        sql_alter_table += sql

    return sql_alter_table

def format_sequence(sequence):
    sql_create_sequence = ""
    for item in sequence:
        sql = '''CREATE sequence {0} INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 \n'''
        sql = sql.format(item)
        sql_create_sequence += sql
        
    return sql_create_sequence