#encoding=UTF-8
import sqlite3, TUtils
import time
def insert(url):
    conn = sqlite3.connect("spider.db")
    mt = TUtils.getRandomByMd5(url, 1)
    ct = int(time.time())
    c = conn.cursor()
    sql = "INSERT INTO tblQueue%d (url, ct)VALUES('%s', %d)"% (mt, url, ct)
    c.execute(sql)
    conn.commit()
    conn.close()

def getByUrl(url):
    conn = sqlite3.connect("spider.db")
    mt = TUtils.getRandomByMd5(url, 1)
    c = conn.cursor()
    sql = "SELECT id FROM tblQueue%d where url='%s'"% (mt, url, )
    c.execute(sql)
    conn.commit()
    row = c.fetchall()
    conn.close()
    return row 
    
