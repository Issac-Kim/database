import sqlite3

f = "discobandit.db"
db = sqlite3.connect(f)
c = db.cursor()

cmd = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;"

info = c.execute(cmd)
students = {}
for item in info:
    students[item[0]] = [item[1], 0.0, 0.0]
info = c.execute(cmd)
for item in info:
    grade = students[item[0]][1] + item[2]
    num_courses = students[item[0]][2] + 1.0
    students[item[0]][1] = grade
    students[item[0]][2] = num_courses
s = "NAME, ID, AVAERAGE\n"
for key in students:
    s += "%s, %d, %f\n" %(key, students[key][0], students[key][1]/students[key][2])
print(s)
    

