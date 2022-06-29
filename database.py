

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
    
conn = sqlite3.connect('data.bd') #connection with db

with conn: # with loop. While this db is open ....
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_data(col_datatype) VALUES (?)", \
                ('information.docx','Hello.txt','myImage.png','myMovie.mpg', \
                 'World.txt','data.pdf','myPhoto.jpg')) # added values to tbl_data
    conn.commit() #saved changes
conn.close() # closed connection


conn = sqlite3.connect('data.db') # connection with db

with conn: # with loop. While this db is open ...
    cur = conn.cursor()
    # selecting all datatype that have 'txt'
    cur.execute("SELECT col_datatype FROM tbl_data WHERE col_datatype LIKE 'txt%'")
    varTxt = cur.fetchall()
    for item in varTxt:
        msg = "txt documents: ()".format(item[0]) #created a variable for all items that were selected
    print(msg) #print variable that has selected file names

