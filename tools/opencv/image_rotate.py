# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 21:42:11 2017
##按照文字方向纠正图像，并对图像进行变换
@author: lywen
"""
import numpy as np
import cv2
from PIL import Image

def Hough(img):
    """
    Hough变换纠正图像的文字方向
    """
    img = cv2.GaussianBlur(img,(3,3),0)##高斯滤波器
    edges = cv2.Canny(img, 50, 150, apertureSize = 3)  
    lines = cv2.HoughLines(edges,1,np.pi/180,118) #这里对最后一个参数使用了经验型的值、
    bata = []
    for line in lines[0][:5].tolist():  
        #rho = line[0] #第一个元素是距离rho  
        theta= line[1] #第二个元素是角度theta  
        if  (theta < (np.pi/4. )) or (theta > (3.*np.pi/4.0)): #垂直直线  
            continue
        else: #水平直线  
            bata.append(theta*180/np.pi -90)
    return np.mean(bata)

def image_rotate(img,prinflag=False,angle=None):
    if angle is None:
       angle = Hough(img)##获取偏移角度
    if prinflag:
        print '图像的纠正角度为:{}'.format(round(angle,3))
    image = Image.fromarray(img)##转化为Image
    image = image.rotate(angle)##图像旋转
    res = np.array(image)##转化为矩阵
    res[res==0]=res.mean()+10##填充旋转后的值
    res = cv2.GaussianBlur(res,(5,5),0)##高斯滤波器
    return res
    
  