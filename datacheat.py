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
print(arr[5:])    #almost same as lists

###### PANDAS #######
import pandas as pd

#SERIES
a = ['a','b','c']
b = [10,20,30]
c = {'d':40,'e':50,'f':60}
print(pd.Series(b,a))       #to create series of datasets
print(pd.Series(c))
#
ser1 = pd.Series([1,2,3,4],index=['India','Russia','Israel','USA'])
print(ser1)           #to create more advanced series of datasets

###### DATAFRAME ########
df = pd.DataFrame
from numpy.random import randn

frame = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])   #randn(5,4) is data frame in structure 5*4
print(frame)      #to frame data in a excel type alignment
#
frame['new'] = frame['W'] + frame['Y']        #to add new column to 'frame'
print(frame)
#
print(frame.drop('Z',axis=1))         #to delete 'Z' column. For column we have to mention axis = 1
print(frame.drop('D',axis=0))         #to delete 'D' row. For row we have to mention axis = 0
#
print(frame['W'])            #to grab column 'W'
print(frame.loc['A'])        #to grab row 'A'
print(frame.loc['B','Y'])    #to grab exact data
#
print(frame>0)                #got answer in True or False
#
print(frame[frame['W']>0])                      #to print the dataframe where 'W' is greater than 0
print(frame[frame['W']>0 & (frame['Y']>1)])     #to print the dataframe where 'W' > 0 and 'Y' > 1
#
new_index = 'CA NY WY OR CO'.split()
print(new_index)
frame['States'] = new_index             #to make new column 'States' ith new index
print(frame)
