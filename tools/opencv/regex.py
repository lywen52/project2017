# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 23:52:20 2017
模糊查询算法实现最优匹配
@author: lywen
"""
def fuzzy_finder(userInput, collection):
    """
    测试用户输入的单词与collection的匹配度
    """
    userDict={}
    for user  in userInput:
         get_num(user,collection,userDict)
         
    return get_max_word(userDict)


def get_num(s,collection,userDict):
    """统计字符串s在每个单词中是否出现"""
    for word in collection:
        if s in word:
           if userDict.get(word) is None:
               userDict[word] = 0
           userDict[word]+=1
           
def get_max_word(userDict):
    """筛选出现频率最大的字符串"""
    return sorted(userDict.items(),reverse=True,key=lambda x:x[1])[0]
 
