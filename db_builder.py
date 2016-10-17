import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O



f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

file1 = open ("peeps.csv")
dict1 = csv.DictReader(file1)

q = "CREATE TABLE students (name TEXT, id INTEGER)"
c.execute(q)

for item in dict1:
    name = item['name']
    id = item['id']
    q = "INSERT INTO students VALUES('" + name + "','" +id + "');"
    c.execute(q)

file2 = open ("courses.csv")
dict2 = csv.DictReader(file2)

q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
c.execute(q)

for item in dict2:
    code = item['code']
    id = item['id']
    mark = item['mark']
    q = "INSERT INTO courses VALUES('" + code + "','" + id + "','" + mark + "');"
    c.execute(q)

#==========================================================
db.commit() #save changes
db.close()  #close database


