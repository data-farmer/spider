#encoding=UTF-8
import TConst as const, TUtils 
import sys, time
import Queue, threading
import IQueueDb as queuedb
import IResult as resultdb

#const.TIME_OUT = 1000
#print const.TIME_OUT

gQueue = Queue.Queue()
def put_htm(htms):
	for htm in htms:
		item = queuedb.getByUrl(htm)
		if not item:
			gQueue.put(htm)
			queuedb.insert(htm)
			allLinks = TUtils.getLinksFromUrl(htm)
			put_htm(allLinks['htm'])

def get_htm(name):
	while True:
		htm = gQueue.get()
		print "线程(%s)正在处理链接: %s"% (name, htm)
		#保存该网页中图片
		allLinks = TUtils.getLinksFromUrl(htm)
		TUtils.saveImg(htm, allLinks['img'])
		#对该网页进行解析存储
		resultdb.insert(htm)

if(len(sys.argv) <2):
    print "No start url..."
    sys.exit() 

startUrl = sys.argv[1]
#1个线程写队列，4个线程读取队列处理数据
threads = [] 
threads.append(threading.Thread(target=put_htm, args=((startUrl,), )))
threads.append(threading.Thread(target=get_htm, args=('p1', )))
threads.append(threading.Thread(target=get_htm, args=('p2', )))
threads.append(threading.Thread(target=get_htm, args=('p3', )))
threads.append(threading.Thread(target=get_htm, args=('p4', )))
for t in threads:
	t.setDaemon(True)
	t.start()
t.join()
