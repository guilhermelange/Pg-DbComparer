def check_tables(table1, table2):
    create_table = []
    for table in table1:
        if not(table in table2):
            create_table.append(table)
    return create_table

def check_sequence(sequence1, sequence2):
    create_sequence = []
    for sequence in sequence1:
        if not(sequence in sequence2):
            create_sequence.append(sequence)
    return create_sequence


def validate_column(current, columns):
    check = True
    try:
        dbColumns = columns.get(current['table_name'])
        for item in dbColumns:
            if item['column_name'] == current['column_name']:
                check = False
                break
    except:
        check = True
    return check

def check_column(columns1, columns2):
    create_columns = []
    for table, columns in columns1.items():
        if table in columns2: # Tabela já existe no destino, caso contrário criará a tabela inteira
            for column in columns: # Tabela objetivo
                if validate_column(column, columns2):
                    create_columns.append(column)
    return create_columns