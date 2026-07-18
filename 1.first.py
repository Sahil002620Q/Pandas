import pandas as pd

data = ['Create','Read','Update','Read']

series = pd.Series(data,index = ['C','R','U','D'])
print(series) #panda series

#change value
series.loc['C'] = 'CREATE'

print(series.loc['C'])    # loc -> location (by real index)
print(series.iloc[0])   # iloc -> integer location (always by 0 indexing)

dict_data = {'key':'val'}

series_x2 = pd.Series(dict_data)
print(series_x2)
print(series_x2.iloc[0])   #no indexing jut key value or iloc