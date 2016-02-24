#encoding=UTF-8
import sqlite3
def create_image():
    conn = sqlite3.connect("spider.db")
    c = conn.cursor()
    for i in range(10):
        sql = 'CREATE TABLE tblImage'+str(i)+' (id INTEGER primary key AUTOINCREMENT,url text, img text, ct int)'
        c.execute(sql)
    conn.commit()
    conn.close()

create_image()
