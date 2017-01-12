# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 20:54:45 2017

@author: lywen
"""
import numpy as np
def image_cut(img,crop):
    """
    剪切图像
    crop=(x0,y0,x1,y1)切割区域,对角线区域，(x0,y0)矩形左上角顶点，(x1,y1)右下角顶点
    """
    return img.crop(crop)

def imgage_split_X(img,n,flag='math'):
    """
    对图像进行垂直等分分割,并生成迭代器
    """
    dimX,dimY = img.size##X，Y轴
    if flag=='math':
        splitList = math_split(img)##数学方法对图像进行分割
    else:
        splitList = split(dimX,n)
    #imgList = []
    for lst in splitList:
        x0 = lst[0]
        x1 = lst[1]
        y0 = 0
        y1 = dimY
        yield image_cut(img,(x0,y0,x1,y1))

        
def imgage_split_Y(img,n,flag='math'):
    """
    对图像进行水平等分分割,并生成迭代器
    """
    dimX,dimY = img.size##X，Y轴
    if flag=='math':
        splitList = math_split(img)##数学方法对图像进行分割
    else:
        splitList = split(dimY,n)
    #imgList = []
    for lst in splitList:
        y0 = lst[0]
        y1 = lst[1]
        x0 = 0
        x1 = dimX
        yield image_cut(img,(x0,0 if y0-20<0 else y0-20,x1,y1-15))
        
    
def split(num,n):
    """对数字进行等分分割N份，并生成
    n:分割等份
    """
    splitList = []
    length = num/n
    for i in range(n):
        splitList.append((length*i,length*(i+1)))
    return  splitList
    
import uuid
def write_image( path, iterList,names):
    i=0
    
    for iterImage in iterList:
        iterImage.save(path+'/'+uuid.uuid1().__str__()+'_'+names[i]+'.jpg')
        i+=1

def math_split(img):
    """运用统计方法分割"""
    array = np.array(img.convert('L'))
    y = array.min(axis=0)
    avg = y.mean()
    y[y>avg] = 255
    y[y<=avg] = 0
    y = y.tolist()
    interval = [[0]]
    val = 5
    for i in range(len(y)-1):
        if y[i]==0 and y[i+1]==255:
           interval.append([interval[-1][-1]+val,i])
    if interval[-1][-1]!=len(y)-1:
        interval[-1][-1] = len(y)-1
    return interval[1:]

