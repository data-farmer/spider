#encoding=UTF-8
import urllib2, re
import TImageDb as imgdb
import time

'''
保存图片信息
存储image
按img进行0～9分表
id 
url: 源网页
img: image地址, 保存最新的一次
ct: 抓取时间
'''
def saveImg(url, imgs):
    for img in imgs:
        item = imgdb.getByImg(img)
        if not item :
            imgdb.insert(url, img,int(time.time())) 
        else :
            pass
'''
根据一个网页获取其摘要信息和标题信息
'''
def getInfoByUrl(url):
    result = {"title": "title", "abstract":""}
    try:
        html = urllib2.urlopen(url, timeout = 5).read()
        title = re.findall(r"<title>(.*)</title>", html)
        title = title[0]
        result['title'] = title 
    except Exception, e:
        pass
    return result

'''
计算一个字符串的md5值
'''
def md5(str):
    import hashlib, types
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ""

def getRandomByMd5(str, num):
    mj = md5(str)
    return int(mj[0:8], 16)%num
'''
获取一个url的类型
'''
def getUrlType(url):
    try:
        page = urllib2.urlopen(url, timeout = 1)
        info = page.info()
        if not info.has_key('Content-Type'):
            return -1 #无法识别 
        ctype = info['Content-Type'] 
        if "text/html" in ctype: #HTML
            return 1 
        elif "image/jpeg" in ctype or "image/png" in ctype: #IMAGE
            return 2
        else: #其他类型
            return 3
    except Exception, e:
        return -1 #url解析错误
'''
正则校验一个url是否符合要求
'''
def checkVaildUrl(url):
    return re.search(r'^(http|https)', url) 

'''
根据一个url获取url中的链接
'''
def getLinksFromUrl(url):
    links = {"htm":[], 'img':[]}
    try:
        page = urllib2.urlopen(url, timeout = 1)
        info = page.info()
        if not info.has_key('Content-Type'):
            return links 
        if "text/html" in info['Content-Type']:
            html = page.read() 
            pattern = re.compile(r'(href|src)=(\'|")(.+?)\2')
            urls = re.findall(pattern, html)
            for i, j, url in urls:
                if checkVaildUrl(url):
                    urlType = getUrlType(url)
                    if urlType == 1:
                        links['htm'].append(url)
                    elif urlType == 2:
                        links['img'].append(url)
                    else:
                        pass
        else:
            pass
        return links
    except Exception, e:
        return links
    
    return links
