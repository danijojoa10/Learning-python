'''
Dev: Silvio Jojoa.
Script description: creation of the CRUD for insert data to database school.db
'''


# C => Create (INSERT INTO)
# R => Read   (SELECT)
# U => Update (UPDATE)
# D => Delete (DELETE)

from school_db import con, cur, sqlite3
import os
import bcrypt

status_menu = True

def crud(op):
    if op == '1':
        # Crear un tipo de identificación
        os.system('clear')

        print("::: Create Identification Type :::")
        name = input("Enter name: ")
        abrev = input("Enter abbreviation: ")
        descrip = input("Enter description: ")

        identificationTypes_table = f'''
            INSERT INTO 
                identificationTypes (name, abrev, descrip) 
                VALUES('{name}', '{abrev}', '{descrip}')
        '''
        cur.execute(identificationTypes_table)
        con.commit()

        print("::: New identification type has been created successfully :::")
        os.system('pause')
        menu()
        
    elif op == '2':
        # Crear una persona
        os.system('clear')

        print("::: Create Person :::")
        fname = input("Enter your first name: ")
        lname = input("Enter your last name: ")
        idNumber = input("Enter your ident number: ")
        address = input("Enter your address: ")
        mobile = input("Enter your mobile: ")

        persons = f'''
            INSERT INTO 
                persons (firstname, lastname, identNumber, address, mobile) 
                VALUES('{fname}', '{lname}', '{idNumber}', '{address}', '{mobile}')
        '''
        cur.execute(persons)
        con.commit()

        print("::: New person has been created successfully :::")
        os.system('pause')
        menu()
    
    elif op == '3':
        # Crear ciudad
        os.system('clear')

        print("::: Create city :::")
        cname = input("Enter name of your city: ")
        cabrev = input("Enter abreviation of your city: ")
        cdescrip= input("Enter description of your city: ")

        cities = f'''
            INSERT INTO 
                cities (name, abrev, descrip) 
                VALUES('{cname}', '{cabrev}', '{cdescrip}')
        '''
        cur.execute(cities)
        con.commit()

        print("::: New city has been created successfully :::")
        os.system('pause')
        menu()
    
    elif op == '4':
        # Crear departamento
        os.system('clear')

        print("::: Create department :::")
        dname = input("Enter name of your department: ")
        dabrev = input("Enter abreviation of your department: ")
        ddescrip= input("Enter description of your department: ")

        departments = f'''
            INSERT INTO 
                departament (name, abrev, descrip) 
                VALUES('{dname}', '{dabrev}', '{ddescrip}')
        '''
        cur.execute(departments)
        con.commit()

        print("::: New department has been created successfully :::")
        os.system('pause')
        menu()

    elif op == '5':
    # Crear pais
        os.system('clear')

        print("::: Create country :::")
        coname = input("Enter name of your country: ")
        coabrev = input("Enter abreviation of your country: ")
        codescrip= input("Enter description of your country: ")

        countries = f'''
            INSERT INTO 
                countries (name, abrev, descrip) 
                VALUES('{coname}', '{coabrev}', '{codescrip}')
        '''
        cur.execute(countries)
        con.commit()

        print("::: New user has been created successfully :::")
        os.system('pause')
        menu()
          
    elif op == '6':
    # Crear usuario
        os.system('clear')

        print("::: Create user :::")
        usemail = input("Enter email of your user: ")
        passwd = input("Enter password of your user: ")

        users = f'''
            INSERT INTO 
                users (email, Password) 
                VALUES('{usemail}', '{passwd}')
        '''
        cur.execute(users)
        con.commit()

        print("::: New user has been created successfully :::")
        os.system('pause')
        menu()

    elif op == '7':
    # Crear estudiante
        os.system('clear')

        print("::: Create student :::")
        ecode = input("Enter your code of student: ")
        cur.execute("SELECT * from persons")

        students = f'''
            INSERT INTO 
                students (code) 
                VALUES('{ecode}')
        '''
        cur.execute(students)
        con.commit()

        print("::: New user has been created successfully :::")
        os.system('pause')
        menu()

def menu():
    global status_menu
    while status_menu: 
        os.system('clear')
        print(":::::::::::::::::::::::")
        print(":::::: MAIN MENU ::::::")
        print(":::::::::::::::::::::::")
        print("[1]. Create identification type")
        print("[2]. Create person")
        print("[3]. Create city")
        print("[4]. Create department")
        print("[5]. Create country ")
        print("[6]. Create user")
        print("[7]. Create student")
        print("[8]. Exit")


        opt = input("Press an option: ")
        if opt == '8':
            print("::: See you soon")
            status_menu = False
            break
        crud(opt)
menu()

# Cerrar la conexión
con.close()