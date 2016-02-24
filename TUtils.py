#encoding=UTF-8
import urllib2, re
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
    except Exception, e:
        print 'Exception', e, url
        return -1 #url解析错误
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
'''
正则校验一个url是否符合要求
'''
def checkVaildUrl(url):
    return re.search(r'^(http|https)', url) 

'''
根据一个url获取url中的链接
'''
def getLinksFromUrl(url):
    try:
        page = urllib2.urlopen(url, timeout = 1)
    except Exception, e:
        print "exception", e, url
    info = page.info()
    links = {"htm":[], 'img':[]} 
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
                    print "htm: %s"% url
                elif urlType == 2:
                    links['img'].append(url)
                    print "img: %s"% url
                else:
                    pass
    else:
        pass
    return links
