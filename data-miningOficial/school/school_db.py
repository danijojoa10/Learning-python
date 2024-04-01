'''
Dev: Silvio Jojoa.
Script description: Configure SQLite3 data base
'''

#Import engine database package
import sqlite3

#Create a database connnection (Database name)
con = sqlite3.connect('school.db')

#Creating cursor object by conection => Let us execute sql commands or operations (Query)
cur = con.cursor()

#Create users table
students_table = '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        code VARCHAR(50) NOT NULL,
        idPerson INTEGER,
        status BOOLEAN DEFAULT true,
        createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        updateAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        deletedAt DATETIME DEFAULT NULL,
        FOREIGN KEY (idPerson) REFERENCES persons(idPerson)
    );
'''

identificationTypes_table = '''
    CREATE TABLE IF NOT EXISTS identificationTypes (
        idIdTy INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        updateAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        deletedAt DATETIME DEFAULT NULL
    );    
'''

countries_table = '''
    CREATE TABLE IF NOT EXISTS countries (
        idCountry INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        updateAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        deletedAt DATETIME DEFAULT NULL
    );    
'''

departament_table = '''
    CREATE TABLE IF NOT EXISTS departament (
        idDep INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        idCountry INTEGER,
        createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        updateAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        deletedAt DATETIME DEFAULT NULL,
        FOREIGN KEY (idCountry) REFERENCES country(idCountry)
    );
'''

cities_table = '''
    CREATE TABLE IF NOT EXISTS cities (
        idExpCity INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        abrev VARCHAR(10) NOT NULL,
        descrip VARCHAR(10) NOT NULL,
        idDep INTEGER,
        createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        updateAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        deletedAt DATETIME DEFAULT NULL,
        FOREIGN KEY (idDep) REFERENCES departaments(idDep)
    );   
'''

users_table = '''
    CREATE TABLE IF NOT EXISTS users (
        idUser INTEGER PRIMARY KEY,
        email VARCHAR(100) NOT NULL,
        Password VARCHAR(250) NOT NULL,
        status BOOLEAN DEFAULT true,
        createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        updateAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        deletedAt DATETIME DEFAULT NULL
    );   
'''

persons_table = '''
    CREATE TABLE IF NOT EXISTS persons (
        idPerson INTEGER PRIMARY KEY,
        firstName VARCHAR(50) NOT NULL,
        lastName VARCHAR(50) NOT NULL,
        idIdTy INTEGER, 
        identNumber VARCHAR(15) NOT NULL,
        idExpCity INTEGER,
        address VARCHAR(150) NOT NULL,
        mobile VARCHAR(50) NOT NULL,
        idUser INTEGER,
        createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        updateAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        deletedAt DATETIME DEFAULT NULL,
        FOREIGN KEY (idIdTy) REFERENCES identificationTypes(idIdTy),
        FOREIGN KEY (idExpCity) REFERENCES cities(idExpCity),
        FOREIGN KEY (idUser) REFERENCES users(idUser)
    );    
'''

#Execute SQL (Query)
cur.execute(students_table )
cur.execute(identificationTypes_table)     
cur.execute(countries_table)
cur.execute(departament_table)
cur.execute(cities_table)
cur.execute(users_table)
cur.execute(persons_table)


#Save changes in database => Push to database
con.commit()

print("::: Database market has been created :::")

#Close connection
#con.close()