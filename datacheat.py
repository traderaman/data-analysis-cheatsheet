###### NUMPY ######
import numpy as np

#ARRAY RANGE IN NUMPY
print(list(range(0,11,2)))
#or
print(np.arange(0,11,2))
#
arr = np.arange(0,11)
print(arr+arr)
print(arr*arr)
print(arr-arr)
print(np.sqrt(arr))
print(np.max(arr))

#NUMPY INDEXING AND SLICING
print(arr[8])
print(arr[1:5])
print(arr[5:])                  #almost same as lists

###### PANDAS #######
import pandas as pd

#SERIES
a = ['a','b','c']
b = [10,20,30]
c = {'d':40,'e':50,'f':60}
print(pd.Series(b,a))           #to create series of datasets
print(pd.Series(c))
#
ser1 = pd.Series([1,2,3,4],index=['India','Russia','Israel','USA'])
print(ser1)                                                           #to create more advanced series of datasets

###### DATAFRAME ########
df = pd.DataFrame
from numpy.random import randn

frame = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])   #randn(5,4) is data frame in structure 5*4
print(frame)                                                               #to frame data in a excel type alignment
#
frame['new'] = frame['W'] + frame['Y']                                     #to add new column to 'frame'
print(frame)
#
print(frame.drop('Z',axis=1))         #to delete 'Z' column. For column we have to mention axis = 1
print(frame.drop('D',axis=0))         #to delete 'D' row. For row we have to mention axis = 0
#
print(frame['W'])            #to grab column 'W'
print(frame.loc['A'])        #to grab row 'A'
print(frame.loc['B','Y'])    #to grab exact data
#
print(frame>0)               #got answer in True or False
#
print(frame[frame['W']>0])                      #to print the dataframe where 'W' is greater than 0
print(frame[frame['W']>0 & (frame['Y']>1)])     #to print the dataframe where 'W' > 0 and 'Y' > 1
#
new_index = 'CA NY WY OR CO'.split()
print(new_index)
frame['States'] = new_index                     #to make new column 'States' ith new index
print(frame)

####### MATPLOTLIB #######
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0,11)
y = x ** 2

plt.plot(x,y)             #to plot x and y
#
plt.xlabel('X label')     #to label X axis
plt.ylabel('Y label')     #to label Y axis
plt.title('TITLE')        #to add a title to the plot
plt.show()                #to show the graph of plot

# TO PLOT MORE THAN ONE PLOT ON SAME WINDOW
plt.subplot(1,2,1)        # here '1' = no. of row, '2' = no. of column, '1' is plot number
plt.plot(x,y,'r')         # here 'r' is colour of line plot i.e. red  
plt.subplot(1,2,2)
plt.plot(y,x,'b')         # instead of 'b' we can use "color = '#FF8C00'" OR "color = 'blue'"
plt.show()

# TO ADD LEGEND
plt.plot(x,y)          
plt.plot(x,y,label= 'legend')
plt.legend()
plt.show()

###### DATETIME #####
from datetime import datetime

year = 2017
month = 1
day = 2
hour = 13
minute = 30
second = 15
date = datetime(year,month,day,hour,minute, second = second)
print(date)

# PLOT MOVING AVERAGES
df = pd.read_csv('walmart_stock.csv')

df['Close'].plot(figsize = (16,6))     #to plot line chart of 'close' column
print(df.rolling(7).mean().head(20))   #to print rolling mean(average) datas of Wallmart

df['Close'].plot()                              #to plot 'Close' data on chart
df['21 MA'] = df['Close'].rolling(21).mean()    #to plot 21 period(rolling) average(mean)
df['21 MA'].plot()                              #to plot 21 MA
plt.show()
