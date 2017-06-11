# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:46:43 2017

@author: Bana
"""
import numpy
from csv import reader
import urllib
import matplotlib
import statistics

risk=[]
laba=[]
CV=[]
ticker=input("Input stock ticker: ").strip().split()
clsprc=[[] for i in range(len(ticker))]
date=[[] for i in range(len(ticker))]
#getting data from google.com/finance and store it to lists      
for i in range(len(ticker)):    
    url="https://www.google.com/finance/historical?output=csv&q="+ticker[i]
    stock=ticker[i]+".csv"
    urllib.request.urlretrieve (url, stock)    
    with open(stock,'r') as f:
        next(f)
        data=list(reader(f))
    clsprc[i]=[float(x[4]) for x in reversed(data)] 
      
for i in range(len(ticker)):
    matplotlib.pyplot.plot(clsprc[i], label=ticker[i].upper())
    risk.append(statistics.stdev(clsprc[i]))
    x=[i for i in range(len(clsprc[i]))]
    l=numpy.polyfit(x,clsprc[i],1)
    laba.append(l[0])
    CV.append(risk[i]/l[0])
    
matplotlib.pyplot.legend(loc='upper left')

for i in range(len(ticker)):
    print ("%s risk: %.2f %% return %.2f %% CV: %.2f" %(ticker[i].upper(),risk[i],laba[i]*100,CV[i])) 


  
