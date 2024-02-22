############# process CSV file, upload data to local posgres database

import pandas as pd
import csvkit
import psycopg2

# no of columns to keep, id column tested to remove null values, additional columns to drop
columns_threshold = 24  
id_column='id'
columns_to_drop = ['Asn - deamidation risk Cnt','BY_PROTEINS','LAST_UPDATER.1','Format']

# input path to CSV file read in CSV, drop columns > columns_threshold, drop additional columns, set up file path for processed CSV
file = input("Input the root address to CSV file, e.g. C:/Downloads/file.csv:")
file = file.replace('\\', '/')
df = pd.read_csv(file, low_memory=False)
df = df.iloc[:, :columns_threshold + 1]
df = df.drop(columns=columns_to_drop, axis=1)
file_processed=file.replace(".","-processed.")

# remove rows where 'id' is null or NaN
df = df[df[id_column].notna()]

# sql to retrieve data
sql="select * from system_engineer_question limit 10"

# edit column names for postgres compatibility
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace('-', '_')
df.columns = df.columns.str.replace('.', '_')
if 'ID' in df.columns and len('ID') == 2:
    df.columns = df.columns.str.replace('id', 'id_')

# save -processed CSV file in the same folder
df.to_csv(file_processed, index=False)

# generate CREATE TABLE code for postgres
create_table_code = f"CREATE TABLE system_engineer_question (\n"
for column_name, data_type in zip(df.columns, df.dtypes):
    if str(data_type) == 'object':
        if df[column_name].str.match(r'\d{2}/\d{2}/\d{4}').all():
            create_table_code += f"    {column_name} DATE,\n"
        else:
            create_table_code += f"    {column_name} TEXT,\n"
    elif str(data_type) == 'int64':
        create_table_code += f"    {column_name} INTEGER,\n"
    elif str(data_type) == 'float64':
        create_table_code += f"    {column_name} FLOAT,\n"
create_table_code = create_table_code.rstrip(',\n') + "\n);"

# generate DATA IMPORT code for postgres
copy_sql = f"""
           COPY {'system_engineer_question'} FROM stdin WITH CSV HEADER
           DELIMITER as ','
           """

# connect to your PostgreSQL database
conn = psycopg2.connect(
    host = input("Connecting to PosgresSQL database - input host, e.g. localhost:"),
    database = input("Input database, e.g. posgres:"),
    user = input("Input user, e.g. postgres"),
    password = input("Input password:")
)
# create cursor object
cur = conn.cursor()

# create table
string = input("Create a new 'system_engineer_question' table in database? (Yes/No)")
if string == "Yes":
    cur.execute(create_table_code) 
    print("New table created")
else: print("No new table")

# import data
string = input("Import data to PosgreSQL? (Yes/No)")
if string == "Yes":
    with open(file_processed, 'r') as f:
        cur.copy_expert(sql=copy_sql, file=f)
        print("Data imported")
else: print("No data import")

# retrieve and print data
string = input("Retrieve example 10 data rows from 'system_engineer_question' (Yes/No)")
if string == "Yes":
    cur.execute(sql) 
    rows = cur.fetchall()
    for row in rows:
        print(row)
else: print("No data retrieval")

# commit
conn.commit()

# close the cursor and connection
cur.close()
conn.close()


