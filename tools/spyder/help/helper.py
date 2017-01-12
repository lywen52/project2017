# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 17:16:23 2016
帮助模块
@author: lywen
"""
import datetime as dt
import re
#import traceback
import time

def timesleep(timeout):
    """
    程序休眠时间
    """
    time.sleep(timeout)

def getNow(format="%Y-%m-%d %H:%M:%S"):
    """
    获取当前时间，按照规定的格式返回
    """
    Now = dt.datetime.now().strftime(format)
    return Now
    
def getNowdelta(delta=1,format="%Y-%m-%d"):
    """
    获取当前时间延迟delta天的日期
    """
    Now = (dt.datetime.now() - dt.timedelta(delta)).strftime(format)
    return Now
    
    
def strTostr(s,format1="%Y-%m-%d %H:%M:%S",format2="%Y-%m-%d %H:%M:%S"):
    """
    将format1 格式转化为 format2
    
    """
    
    try:
       return  dt.datetime.strptime(s,format1).strftime(format2)
        
    except:
        return None

def listsplit(Lst,splitnum):
    """
    对列表进行均等分割
    splitnum:分割份数
    """
    spacelist = []
    length = len(Lst)
    if splitnum<=1 or length< splitnum:
        return [Lst]
    else:
        
        num  = length / splitnum 
        
        
        for i in range(splitnum):
            spacelist.append(Lst[i*num:(i+1)*num])
        
        if length % splitnum>0:
             spacelist[-1].extend(Lst[(i+1)*num:])
        return spacelist
        
def urlpath(url):
    """
    url = http://webforex.hermes.hexun.com/forex/kline?code=FOREXAUDCAD&start=201607151000&number=1&type=0
    从url 中解析出code,type    
    """
    code = re.findall('code=\w*',url)
    types = re.findall('type=\w*',url)
    if len(code)>0:
        code = code[0].replace('code=FOREX','')
    if len(types)>0:
        types = types[0].replace('type=','')
        
    return code,types
    
    
def strTofloat(string,types=float):
    """
    字符串转换为数字
    """
    try:
        return types(string.replace(',','').replace(u'，',''))
    except:
        #traceback.print_exc()
        return None