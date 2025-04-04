import csv
import sqlite3 as s

conn=s.connect("C:\Users\lelay\Desktop\PIkemon")
cur=conn.cursor()

types = [("normal","6 8 9",""),
         ("fighting","3 4 7 8 14 18","1 6 9 15 17"),
         ("flying","6 9 13","2 7 12"),
         ("poison","4 5 6 8 9","12 18"),
         ("ground","3 7 12","4 6 9 10 13"),
         ("rock","2 5 9","3 7 10 15"),
         ("bug","2 3 4 8 9 10 18","12 14 17"),
         ("ghost","1 17","8 14"),
         ("steel","9 10 11 13","6 15 18"),
         ("fire","6 10 11 16","7 9 12 15"),
         ("water","11 12 16","5 6 10"),
         ("grass","3 4 7 9 10 12 16","5 6 11"),
         ("electric","5 12 13 16","3 11"),
         ("psychic","9 14 17","2 4"),
         ("ice","9 10 11 15","3 5 12 16"),
         ("dragon","9 18","16"),
         ("dark","2 17 18","8 14"),
         ("fairy","4 9 10","2 16 17")]
#cur.execute("CREATE TABLE TYPES (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,coefneg TEXT, coefpos TEXT)")

#update pikemon pr cle etrangere type + attack
cur.execute("UPDATE TABLE PIKEMON SELECT ")
cur.executemany("INSERT INTO TYPES(name,coefneg,coefpos) VALUES(?,?,?)",types)

conn.commit()

cur.close()
conn.close()
