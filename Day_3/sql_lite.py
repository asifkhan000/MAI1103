#import sql library
import sqlite3

#connect a file or create a csv..
conn = sqlite3.connect('emoployes.db')

#create table
c.Execute("""CREATE TABLE employees(ID INTEGER, first TEXT, pay INTEGER)""")


#INERT DATA INTO TABLE
c.execute("INSERT INTO employees VALUES(02,'ASIF','UNVIVERSITY',50000000")


#SELECT QUERY
c.execute("SELECT * FROM employees")

#print 
print(c.fetchone())
