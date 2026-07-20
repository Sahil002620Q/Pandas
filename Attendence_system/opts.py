from datetime import datetime
import pandas as pd

def decorate(option,*arg,**kwarg):
    def wrap():
        print("================================")
        option()
        print("================================")
    return wrap

def cls():
    import os
    os.system("clear")

def dateTime_today():
    dateTime = datetime.now()   # return yy/mm/dd hr:min:sec.milisec
    return dateTime             # dateTime() = 00/00/00 00:00:00.000
 
def date_today():
    dt = dateTime_today()       # calling fun coz 
    date = dt.strftime("%d/%m/%y")
    print(date)                # date_today() = 00/00/00


data = {'math':15, 'dsa':19,'oops':17,'D.E.':14}

series = pd.Series(data,dtype='int64')


def inc_sub_attendence(subject):
    series.loc[subject] += 1

def att(sub):
    try:
        inc_sub_attendence(sub)
    except KeyError:
        print("invailed subject : ",sub)

def ctnue():
    input("Press Enter to continue : ")


#-----for incriment of attendence
x = "lib"

if __name__ == "__main__":
    dateTime_today()
    date_today()
    print(series.loc[series > 20])
    @decorate
    def m():
        print(x)
    m()


    # def choiceval():
    # try:
    #     choice_for_comp()
    # except:
    #     print("type error")