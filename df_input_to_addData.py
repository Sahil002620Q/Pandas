import pandas as pd 

excel = {'name':[],'age':[],'job':[]}

df = pd.DataFrame(excel) #made a data frame
#add row (new user data ie new name age and coding for new user)

name = input("Enter your name : ")
age = input("Enter your age : ")
job = input("Enter your job : ")
income = input("Enter your income : ")
new_user = pd.DataFrame([{'name': name ,'age': age ,'job': job}],index=['student 2']) # send as non list  [] represent whole row

#add new user to df
df = pd.concat([df, new_user]) 
df['income'] = ['2k']
print(df)

