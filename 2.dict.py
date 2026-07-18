import pandas as pd

def inc_sub_attendence(subject):
    series.loc[subject] += 1

def att(sub):
    try:
        inc_sub_attendence(sub)
    except KeyError:
        print("invailed subject : ",sub)


data = {'math':15, 'dsa':19,'oops':17,'D.E.':14}

series = pd.Series(data,dtype='int64')
print(series.loc[series > 20]) #compare attendence , check for low and high or max usecase everywhere ie check attendence , 

print(series)

#################loc location by lable if i change idex with 's' i labled it with s 

#increase attendence by one (use normally )
# series.loc['math'] += 1   # increase attendence by one (make it in func form and call when inc or dec)
# series.loc['dsa'] += 1    #func take sub arg and will inc or dec for only that 
# series.loc['oops'] += 1
# series.loc['D.E.'] += 1
att('math')
att('dsa')
att('oops')
att('D.E.')
att('bug.....')

# try:
#     inc_sub_attendence('bug........')
# except KeyError:
#     print("invailed subject")


#dec attendence one marked wrong call it so u can undo
# series.loc['math'] -= 1   # increase attendence by one
# series.loc['dsa'] -= 1
# series.loc['oops'] -= 1
# series.loc['D.E.'] -= 1



print(series)