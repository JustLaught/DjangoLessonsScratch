#DB API 
import psycopg2
import os

PASS = os.environ.get("DB_PASS")
connectoin = psycopg2.connect(host="localhost", user="postgres", database="Hospital", password=PASS)
cursor = connectoin.cursor()
# WORK WITH DB
cursor.execute('SELECT * FROM public."Doctors";')
cursor.execute('SELECT * FROM public."Departments";')

# result = cursor.fetchall()
# result2 = cursor.fetchall()
# print("Id", "Name", "Phone", "Salary", "Surname", "Premium", sep="\t")
# for e in result:
#     print(*e,sep='\t')

# result = cursor.fetchone()
# while result is not None:
#     print(result)
#     result = cursor.fetchone()

# cursor.execute("""INSERT INTO public."Donations" 
#                ("Amount", "Date", "Departmentsid", "Sponsorid") 
#                VALUES 
#                (10000::money, '2023-02-02', 1, 4);
#                """)
# connectoin.commit()

# print("Result2")
# print(result2)
cursor.close()