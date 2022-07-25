from Database import Database
from ReaderUtils import getData
from CheckUtils import check_column, check_sequence, check_tables
from SqlFormatter import format_sequence, format_table, format_table_column

host = '127.0.0.1'
port = 5432
database1 = Database(host, port, 'diff_a', 'postgres', 'postgres')
database2 = Database(host, port, 'diff_b', 'postgres', 'postgres')

table1, sequence1, columns1 = getData(database1)
table2, sequence2, columns2 = getData(database2)

table = check_tables(table1, table2)
sequence = check_sequence(sequence1, sequence2)
columns = check_column(columns1, columns2)

sql_create_table = format_table(table, columns1)
sql_create_column = format_table_column(columns)
sql_create_sequence = format_sequence(sequence)

print(sql_create_table)
print(sql_create_column)
print(sql_create_sequence)