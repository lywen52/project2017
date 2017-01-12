# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:37:10 2017

@author: lywen
##从百度爬取指定内容的图像
"""
import json
import sys
sys.path.append('../request')
from request.request import Request
import time 
import urllib
import uuid

class Handler():
    url ="""http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord+=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&rn=60&gsm=1e&{}="""
    
    def __init__(self, path, word, pages=100):
        """
        path:保存图像到对应的路径
        word:搜索关键词
        pages:搜索的页数
        """
        
        self.path = path
        self.pages = pages
        self.word = word.encode('utf-8') if type(word) is unicode else word
        
        
    def on_search(self):
        """
        搜索图像
        """
        self.urllist = []
        for i in range(self.pages):
                
                params = {'word':self.word,
                          'step_word':self.word,
                          'pn':i
                          }
                params = urllib.urlencode(params)          
                t = int(time.time()*1000)
                
                url = (self.url+params).format(t)
                print url
                headers = {
                          "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"}
                response = self.crawl(url,headers)
                print response
                if response:
                    dList = self.html_clean(response)
                    self.urllist.extend(dList)
                
                


    def crawl(self,url, headers={}, data=None,flag='get'):
        """
        爬取网页
        """
        if flag=='get':
            response = Request(url,headers).urlopen()
        else:
            response = Request(url,headers).post()
        return response
        
    def html_clean(self, response):
        """
        获取页面的图片网址
        """
        data = json.loads(response.text)
        dList = []
        for x in data['data'][:-1]:
            temp = {}
            hoverURL = x.get(u'hoverURL')
            if hoverURL is not None and hoverURL!=u'':
                temp['hoverURL'] = hoverURL
            
            thumbURL =x.get(u'thumbURL')
            
            if thumbURL is not None and thumbURL!=u'':
                temp['thumbURL'] = thumbURL
                
            middleURL =x.get(u'middleURL')
            if middleURL is not None and middleURL!=u'':
                temp['middleURL'] = middleURL
                
                
          
            if x.get(u'replaceUrl') is not None:
                temp['replaceUrl'] =[]
                for y in  x.get(u'replaceUrl'):
                    ObjURL = y.get('ObjURL')
                    if ObjURL is not None:
                        temp['replaceUrl'].append(ObjURL)
            if temp !={}:
                temp.update(response.save) 
                uid = uuid.uuid1().__str__()
                temp.update({'uid':uid})
                dList.append(temp)
        
        return dList
        
                                    
         
        
    def on_result(self, result):
            """存储数据
            """
