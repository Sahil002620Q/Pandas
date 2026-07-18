import pandas as pd 

excel = {'name':['sam'],'age':[20],'job':['coding']}

df = pd.DataFrame(excel,index=['student 1']) #made a data frame
#add row (new user data ie new name age and coding for new user)
new_user = pd.DataFrame([{'name':'samir','age':21,'job':'web dev'}],index=['student 2']) # send as non list  [] represent whole row

#add new user to df
df = pd.concat([df, new_user]) 

#add new column (need to add data for all recent user)
df['income'] = ['20k','15k']

print(df)


