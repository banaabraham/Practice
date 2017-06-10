# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:46:43 2017

@author: lenovo
"""
import numpy
from csv import reader
import urllib
from matplotlib import pyplot as plt
import statistics


ticker=input("Input stock ticker: ")
url="https://www.google.com/finance/historical?output=csv&q="+ticker
print (url)
urllib.request.urlretrieve (url, "stock.csv")

with open('stock.csv','r') as f:
    next(f)
    data=list(reader(f))
datalnt=float(len(data))   
clsprc=[float(x[4]) for x in reversed(data)]
x=numpy.arange(1.,datalnt+1.,1.)
risk=statistics.stdev(clsprc)
plt.plot(x,clsprc)
laba=((clsprc[len(data)-1]-clsprc[0])/clsprc[0])*100
print ("Risk(stdev) %d Return %d" %(risk,laba))

  