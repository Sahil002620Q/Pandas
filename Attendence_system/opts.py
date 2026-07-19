def decorate(option,*arg,**kwarg):
    def wrap():
        print("================================")
        option()
        print("================================")
    return wrap

def cls():
    import os
    os.system("clear")


#-------------------------------------------
import pandas as pd

data = {'math':15, 'dsa':19,'oops':17,'D.E.':14}

series = pd.Series(data,dtype='int64')
print(series.loc[series > 20])

def inc_sub_attendence(subject):
    series.loc[subject] += 1

def att(sub):
    try:
        inc_sub_attendence(sub)
    except KeyError:
        print("invailed subject : ",sub)
#---
def ctnue():
    input("Enter to back to home : ")
#--

#-------------------------for incriment of attendence
x = "lib"

if __name__ == "__main__":
    @decorate
    def m():
        print(x)
    m()


    # def choiceval():
    # try:
    #     choice_for_comp()
    # except:
    #     print("type error")