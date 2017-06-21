import urllib
from csv import reader
import pandas as pd
import numpy as np
import pyqtgraph as pg
from sklearn.svm import SVR

def closeprice(ticker):
    url="https://www.google.com/finance/historical?output=csv&q="+ticker
    stock=ticker+".csv"
    urllib.request.urlretrieve (url, stock)    
    with open(stock,'r') as f:
        next(f)
        data=list(reader(f))
    clsprc=[float(x[4]) for x in reversed(data)]
    return clsprc

def get_data(ticker):
    url="https://www.google.com/finance/historical?output=csv&q="+ticker
    stock=ticker+".csv"
    urllib.request.urlretrieve(url,stock)
    d=pd.read_csv(stock)
    #reverse all but index
    d.iloc[:] = d.iloc[::-1].values
    x=np.arange(1,len(d)+1,1.0)    
    data=[]
    for i in range(len(d)):
        temp=(x[i], d['Open'][i], d['Close'][i], d['Low'][i], d['High'][i])
        temp=tuple(temp)
        data.append(temp)
    return data  

def volume(ticker): 
    url="https://www.google.com/finance/historical?output=csv&q="+ticker
    stock=ticker+".csv"
    urllib.request.urlretrieve(url,stock)
    d=pd.read_csv(stock)
    #reverse all but index
    d.iloc[:] = d.iloc[::-1].values
    #x=np.arange(1,len(d)+1,1.0)
    data=[]
    for i in range(len(d)):
        temp=[float(d['Volume'][i])/1e6]
        data.append(temp)
    return data 
  
  
def prediction(ticker):
    url="https://www.google.com/finance/historical?output=csv&q="+ticker
    stock=ticker+".csv"
    urllib.request.urlretrieve(url,stock)
    d=pd.read_csv(stock)
    d.iloc[:] = d.iloc[::-1].values
    svr_rbf = SVR(kernel= 'rbf', C= 1e3, gamma= 0.1)
    X=np.arange(1,len(d)+1,1.0)
    X=np.reshape(X,(len(X),1))
    y=d['Close']
    y_rbf = svr_rbf.fit(X, y).predict(X)
    return y_rbf
    
    
    
    
    
    
        
        