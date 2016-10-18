import sqlite3

f = "discobandit.db"
db = sqlite3.connect(f)
c = db.cursor()

cmd = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;"

info = c.execute(cmd)
students = {}
for item in info:
    
    student[item[0]] = [item[1], ]
    

