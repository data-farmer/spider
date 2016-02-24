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
    
def create_queue():
    conn = sqlite3.connect("spider.db")
    c = conn.cursor()
    for i in range(1):
        sql = 'CREATE TABLE tblQueue'+str(i)+' (id INTEGER primary key AUTOINCREMENT,url text, ct int)'
        c.execute(sql)
    conn.commit()
    conn.close()

def create_result():
    conn = sqlite3.connect("spider.db")
    c = conn.cursor()
    for i in range(1):
        sql = 'CREATE TABLE tblResult'+str(i)+' (id INTEGER primary key AUTOINCREMENT,url varchar(400), ct int, title varchar(400), abstract text)'
        c.execute(sql)
    conn.commit()
    conn.close()

create_queue() 
create_image()
create_result()
