#encoding=UTF-8
import sqlite3, TUtils
import time
def insert(url):
    conn = sqlite3.connect("spider.db")
    mt = TUtils.getRandomByMd5(url, 1)
    ct = int(time.time())
    info = TUtils.getInfoByUrl(url)
    title = info['title']
    abstract = info['abstract']
    c = conn.cursor()
    sql = "INSERT INTO tblResult%d (url, title, abstract, ct)VALUES('%s', '%s', '%s', %d)"% (mt, url, title, abstract, ct)
    c.execute(sql)
    conn.commit()
    conn.close()
