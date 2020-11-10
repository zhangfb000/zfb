# 爬取当前网站下所有HTML网页

import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    '''
    此函数用于获取网页的html文档
    '''
    try:
        #获取服务器的响应内容，并设置最大请求时间为6秒
        res = requests.get(url, timeout = 6)
        #判断返回状态码是否为200
        res.raise_for_status()
        #设置该html文档可能的编码
        res.encoding = res.apparent_encoding
        #返回网页HTML代码
        return res.text
    except:
        return '产生异常'

def main():
    '''
    主函数
    '''
    #目标网页
    url = 'http://162.105.138.23/bdms/all.htm#l'

    demo = getHTMLText(url)

    #解析HTML代码
    soup = BeautifulSoup(demo, 'html.parser')

    #模糊搜索HTML代码的所有包含href属性的<a>标签
    a_labels = soup.find_all('a', attrs={'href': True})

    #获取所有<a>标签中的href对应的值，即超链接


    for a in a_labels:
        href = a.get('href')
        objectSearch = re.search('mr_index',href)
        if objectSearch:
            base_url = 'http://162.105.138.23/bdms/'   #目标网页
            #print(href)
            req_url = base_url + href
            res = requests.get(req_url, timeout = 6)
            res.encoding = res.apparent_encoding
            res = res.text.encode("gbk",'ignore')
            print(res)
            with open('./html/{}.html'.format(href),'wb') as f:
                f.write(res)
        else:
            pass

main()
