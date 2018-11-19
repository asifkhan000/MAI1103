#import sql library
import sqlite3

#connect a file or create a csv..
conn = sqlite3.connect('emoployes.db')



#connet sqlite
c=conn.cursor()


#create table

c.execute("""CREATE TABLE employees
    (id INTEGER,
    first TEXT,
    last TEXT,
    pay INTEGER
    )""")
        
#INERT DATA INTO TABLE
c.execute("INSERT INTO employees VALUES (10,'asif','UNVIVERSITY',50000000)")


#SELECT QUERY
c.execute("SELECT * FROM employees")


#import sql library
import sqlite3

#connect a file or create a csv..
conn = sqlite3.connect('emoployes.db')



#connet sqlite
c=conn.cursor()


#create table

c.execute("""CREATE TABLE employees
    (id INTEGER,
    first TEXT,
    last TEXT,
    pay INTEGER
    )""")
        
#INERT DATA INTO TABLE
c.execute("INSERT INTO employees VALUES (10,'asif','UNVIVERSITY',50000000)")


#SELECT QUERY
c.execute("SELECT * FROM employees")


