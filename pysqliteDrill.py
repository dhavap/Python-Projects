import sqlite3

#creating the table
conn = sqlite3.connect('sqliteDrill.db')
with conn:  
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT)")
    conn.commit()
conn.close()

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


conn = sqlite3.connect('sqliteDrill.db')
with conn:
        cur = conn.cursor()
        for file in fileList: # iterate through list of files to look for files ending with '.txt' and add items to the table
                if file.endswith('.txt'):  
                    cur.execute("INSERT INTO tbl_files(col_filename) VALUES (?)", (file,) )  # put the 'txt' files into the table
        conn.commit()
conn.close()

conn =  sqlite3.connect('sqliteDrill.db')

with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_filename FROM tbl_files")
        varFiles = cur.fetchall()
        print(varFiles)
        conn.commit()
conn.close()


    

        
                       
    
    

