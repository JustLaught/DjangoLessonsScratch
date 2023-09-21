import psycopg2


connectoin = psycopg2.connect(host="localhost", user="postgres", database="Sales", password="2773")
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

def show_Sellers():
    cursor.execute('SELECT * FROM public."Salesmen"')
    result = cursor.fetchall()
    for e in result:
        print(e)
    print()

def show_Customers():
    cursor.execute('SELECT * FROM public."Customer"')
    result = cursor.fetchall()
    for e in result:
        print(e)
    print()   

while True:
    option = int(input("1)Show ALL | 2)Select by Name | 3)By MAX price | 4)By MIN price\n5)MAX price Salesmen | 6)MIN price Salesmen | 7)MAX price Customer | 8)MIN price Customer\n9)MIN sum ALL | 10)MAX sum ALL | 11)AVG Customer | 12)AVG Salesmen | 0) EXIT\n Enter your option: "))
    print()
    # request = input("Enter request: ")  #"""SELECT FROM public.""  WHERE   ! EXAMPLE !"""
    if option == 1:
        request = 'SELECT * FROM public."Sales"'

    elif option == 2:
        show_Sellers()
        seller_name = input("Enter seller name:  ")
        seller_LastName = input("Enter seller Last Name:  ")
        request = f'SELECT * FROM public."Sales" AS S INNER JOIN public."Salesmen" AS M ON S."SellerID" = M."ID" WHERE M."Name" = \'{seller_name}\' AND M."LastName" = \'{seller_LastName}\''

    elif option == 3:
        request = 'SELECT * FROM public."Sales" WHERE "Price" = (SELECT MAX("Price") FROM public."Sales")'

    elif option == 4:
        request = 'SELECT * FROM public."Sales" WHERE "Price" = (SELECT MIN("Price") FROM public."Sales")'

    elif option == 5:
        show_Sellers()
        seller_name = input("Enter seller name:  ")
        seller_LastName = input("Enter seller Last Name:  ")
        print()
        request = f'SELECT * FROM public."Sales"  WHERE "Price" = (SELECT MAX("Price") FROM public."Sales" AS S INNER JOIN public."Salesmen" AS M ON S."SellerID" = M."ID" WHERE M."Name" = \'{seller_name}\' AND M."LastName" = \'{seller_LastName}\')'

    elif option == 6:
        show_Sellers()
        seller_name = input("Enter seller name:  ")
        seller_LastName = input("Enter seller Last Name:  ")
        print()
        request = f'SELECT * FROM public."Sales"  WHERE "Price" = (SELECT MIN("Price") FROM public."Sales" AS S INNER JOIN public."Salesmen" AS M ON S."SellerID" = M."ID" WHERE M."Name" = \'{seller_name}\' AND M."LastName" = \'{seller_LastName}\')'

    elif option == 7:
        show_Customers()
        custom_name = input("Enter seller name:  ")
        custom_LastName = input("Enter seller Last Name:  ")
        print()
        request = f'SELECT * FROM public."Sales"  WHERE "Price" = (SELECT MAX("Price") FROM public."Sales" AS S INNER JOIN public."Customers" AS C ON S."SellerID" = C."ID" WHERE C."Name" = \'{custom_name}\' AND C."LastName" = \'{custom_LastName}\')'

    elif option == 8:
        show_Customers()
        custom_name = input("Enter seller name:  ")
        custom_LastName = input("Enter seller Last Name:  ")
        print()
        request = f'SELECT * FROM public."Sales"  WHERE "Price" = (SELECT MIN("Price") FROM public."Sales" AS S INNER JOIN public."Customers" AS C ON S."SellerID" = C."ID" WHERE C."Name" = \'{custom_name}\' AND C."LastName" = \'{custom_LastName}\')'

    elif option == 9:
        request = 'SELECT SM."Name", SM."LastName", SUM(S."Price") FROM public."Sales" AS S INNER JOIN public."Salesmen" AS SM ON S."SellerID" = SM."ID" GROUP BY SM."Name", SM."LastName"'

    elif option == 10:
        request = 'SELECT CU."Name", CU."LastName", SUM(S."Price") FROM public."Sales" AS S INNER JOIN public."Customer" AS CU ON S."CustomerID" = CU."ID"GROUP BY CU."Name", CU."LastName"'

    elif option == 11:
        show_Customers()
        custom_name = input("Enter Custumer name:  ")
        custom_LastName = input("Enter Customer Last Name:  ")
        request = f'SELECT CU."Name", CU."LastName", AVG(S."Price") FROM public."Sales" AS S INNER JOIN public."Customer" AS CU ON S."CustomerID" = CU."ID" GROUP BY CU."Name", CU."LastName" HAVING CU."Name" = \'{custom_name}\' AND CU."LastName" = \'{custom_LastName}\''

    elif option == 12:
        show_Sellers()
        seller_name = input("Enter seller name:  ")
        seller_LastName = input("Enter seller Last Name:  ")
        request = f'SELECT SM."Name", SM."LastName", AVG(S."Price") FROM public."Sales" AS S INNER JOIN public."Salesmen" AS SM ON S."SellerID" = SM."ID" GROUP BY SM."Name", SM."LastName" HAVING SM."Name" = \'{seller_name}\' AND CU."LastName" = \'{seller_LastName}\''

    elif option == 0:
        cursor.close()
        break

    cursor.execute(request)
    result = cursor.fetchall()
    for e in result:
        print(e)
        
    print()