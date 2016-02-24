#encoding=UTF-8
import sqlite3, TUtils
def insert(url, image, ct):
    conn = sqlite3.connect("spider.db")
    mt = TUtils.getRandomByMd5(image, 10)
    c = conn.cursor()
    sql = "INSERT INTO tblImage%d (url, img, ct)VALUES('%s', '%s', %d)"% (mt, url, image, ct)
    c.execute(sql)
    conn.commit()
    conn.close()

def getByImg(image):
    conn = sqlite3.connect("spider.db")
    mt = TUtils.getRandomByMd5(image, 10)
    c = conn.cursor()
    sql = "SELECT id FROM tblImage%d where img='%s'"% (mt, image, )
    c.execute(sql)
    conn.commit()
    row = c.fetchall()
    conn.close()
    return row 

    
