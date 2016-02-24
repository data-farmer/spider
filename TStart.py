#encoding=UTF-8
import TConst as const, TUtils 
import sys, time

const.TIME_OUT = 1000
print const.TIME_OUT

if(len(sys.argv) <2):
    print "No start url..."
    sys.exit() 

startUrl = sys.argv[1]
print "start url is: %s, md5 is:%d " %(startUrl, TUtils.getRandomByMd5(startUrl, 10))
'''
摘要表, 按url取md5分表100, id使用全局id
一个url建一张表保存其所有的爬取结果
爬取一个url的摘要
id: 
url: 当前地址
abstract: 摘要
parentid: parent id

ids分配表
name
id
一个线程写队列，一个线程读取队列处理数据
'''
allLinks = TUtils.getLinksFromUrl(startUrl) 
#....使用多线程处理网页 


imgs = allLinks['img']
TUtils.saveImg(startUrl, imgs)
