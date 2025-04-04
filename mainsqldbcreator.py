
import csv
import sqlite3 as s
csv_filename = "TERM\PikemonGame\pokemon.csv"
with open(csv_filename) as f:
    reader = csv.reader(f)
    lst = [list(line) for line in reader]

conn=s.connect("dbpikemon.db")
cur=conn.cursor()

cur.execute("CREATE TABLE PIKEMON (id INTEGER PRIMARY KEY AUTOINCREMENT,id_pikemon INT,Name TEXT,Type1 TEXT,Type2 TEXT,Total INT,HP INT,Attack INT,Defense INT,SpAtk INT ,SpDef INT,Speed INT,Generation INT,Legendary BOOL)")
for elt in lst:
    print(elt)
    t=elt
    t[0]=int(t[0])
    if t[12] == "False":
        t[12] = False
    else:
        t[12] = True
    for i in range(4,12):
        t[i]=int(t[i])
    elt=tuple(t)
    print(elt)
cur.executemany("INSERT INTO PIKEMON(id_pikemon,Name,Type1,Type2,Total,HP,Attack,Defense,SpAtk,SpDef,Speed,Generation,Legendary) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",lst)

conn.commit()

cur.close()
conn.close()
