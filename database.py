

#Database submission assignment

import sqlite3

conn = sqlite3.connect('data.db') #created a database called data.db & made connection

with conn: # with loop. While this database is open ...
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_data( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_datatype TEXT)") #created table, columns and primary key for table in db
    conn.commit() #saved changes
conn.close() #closed connection to db
    
conn = sqlite3.connect('data.db') #connection with db

fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg', \
            'World.txt','data.pdf','myPhoto.jpg')
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_data (col_datatype) VALUES (?)",(x,))
            print(x)
conn.close()
