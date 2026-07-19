import pandas as pd 
import random


data = []  #init empty  list

for i in range(10):   # the below code for 10 times
    generate_random = random.randint(100,999)   #generate random number and add it to data list 
    data.append(generate_random)

print(data)

#apply panda seriex

series = pd.Series(data)
# print(series)

# format series.loc[conditon with series] 
print(series.iloc[series >= 500]) # all greated than 
print(series.iloc[series <= 500])
print(series.iloc[series % 2 == 1])  #print all odd's
print(series.iloc[series % 2 != 1]) #or == 1 will result same , it print all even's


