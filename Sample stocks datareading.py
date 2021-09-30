import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import pandas_datareader
import pandas_datareader.data as web

start = datetime.datetime(2012,1,1)           #start date
end = datetime.datetime(2017,1,1)             #end date

tesla = web.DataReader('TSLA','yahoo',start,end)    #read data from start date to end date
ford = web.DataReader('F','yahoo',start,end)
gm = web.DataReader('GM','yahoo',start,end)

tesla['Open'].plot(label='Tesla',figsize=(16,8), title = 'Open')        #to plot opening prices chart
ford['Open'].plot(label='Ford',figsize=(16,8), title = 'Open')
gm['Open'].plot(label='GM',figsize=(16,8), title = 'Open')
plt.legend()
plt.show()

tesla['Volume'].plot(label='Tesla',figsize=(16,8), title = 'Volume')    #to plot volume chart
ford['Volume'].plot(label='Ford',figsize=(16,8), title = 'Volume')
gm['Volume'].plot(label='GM',figsize=(16,8), title = 'Volume')
plt.legend()
plt.show()

tesla['Total Traded'] = tesla['Open']*tesla['Volume']         #total volume traded during the period
ford['Total Traded'] = ford['Open']*ford['Volume']
gm['Total Traded'] = gm['Open']*gm['Volume']

tesla['Total Traded'].plot(label = 'Tesla',figsize=(16,8))    #to plot total volume traded
ford['Total Traded'].plot(label = 'Ford')
gm['Total Traded'].plot(label = 'GM')
plt.legend()
plt.show()

gm['MA 50'] = gm['Close'].rolling(50).mean()               #to add 50 MA to chart
gm['MA 200'] = gm['Close'].rolling(200).mean()
gm['EMA 21'] = gm['Close'].ewm(21).mean()                  #to add 21 EMA to chart
gm[['Close','MA 50','MA 200']].plot(figsize= (16,8))
plt.legend()
plt.show()

tesla['returns'] = tesla['Close'].pct_change(1)        #to calculate daily returns 
ford['returns'] = ford['Close'].pct_change(1)
gm['returns'] = gm['Close'].pct_change(1)

tesla['returns'].hist(bins = 100,label = 'Tesla',figsize =(16,8))    #to get cumulative daily returns in histogram
ford['returns'].hist(bins = 100,label = 'Ford',figsize =(16,8))
gm['returns'].hist(bins = 100,label = 'gm',figsize =(16,8))
