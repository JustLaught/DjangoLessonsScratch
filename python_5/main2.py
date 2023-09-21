import psycopg2


connectoin = psycopg2.connect(host="localhost", user="postgres", database="Hospital", password="2773")
cursor = connectoin.cursor()

tables = []
request = """
SELECT * 
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND
schemaname != 'information_schema';
"""

cursor.execute(request)
result = cursor.fetchall()
for e in result:
    tables.append(f'{e[0]}."{e[1]}"')
# print(*tables, sep='\n')

request = input("Enter request: ")
elements = request.split()

for i, e in enumerate(elements):
    if e.endswith(";"):
        elements[i] = e[:-1]

flag_table_name = False
for e in elements:
    if e in tables:
        flag_table_name = True

flag_where = False
if elements[0].upper() == "UPDATE" or elements[0].upper() == "DELETE":
    for e in elements:
        if e.upper() == "WHERE":
            flag_where = True
else:
    flag_where = True

if not flag_table_name:
    print('Table name is missing.')

if not flag_where:
    print("Wrong request condition")

if flag_table_name and flag_where:
    cursor.execute(request)
    result = cursor.fetchall()
    for e in result:
        print(e)

cursor.close()