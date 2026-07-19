import pandas as pd
from datetime import datetime
import os 
from opts import decorate,cls,ctnue
from layout import display_menu

##-----------------------------------

data = {'math':0, 'dsa':0,'oops':0,'D.E.':0}
series = pd.Series(data)

print(series.to_string())

#========================================

def inc_sub_attendence(subject):
    series.loc[subject] += 1

def att(sub):  #take inc_sunb_attenecence and check if that subject wxit else thorew error
    try:
        inc_sub_attendence(sub)
    except KeyError:
        print("invailed subject : ",sub)

#+====================================

#---------only attendence----------

def dateTime_today():
    dateTime = datetime.now()   # return yy/mm/dd hr:min:sec.milisec
    return dateTime             # dateTime() = 00/00/00 00:00:00.000
 
def date_today():
    dt = dateTime_today()       # calling fun coz 
    date = dt.strftime("%d/%m/%y")
    print(date)                # date_today() = 00/00/00

# dateTime_today()
# date_today()

def choice():
    try:
        x = int(input())
        # print("working")y
        return x    # pack a choice in variable and call it later for comparison
    except ValueError:
        print("",end='')
#ask ho much lecture today



#menu
    


#================def for options/choice
@decorate  #1st 
def today_att():
    print("todays attendence")
    sub_to_add = int(input("enter total classes you attend today : "))
    if sub_to_add > 8 :
            print("Wrong input ")
    # run loop sub to add time
    #  assume  5

    #empty list
    subx = {}
    for i in range(sub_to_add):
        sub = input("Enter subject : ") 
        attn = input("Mark present/absent : ") #pend logic
        

        if attn == 'p' or 'P' or 1 or 'Present' or 'y' or "YES" or 'yes' or 'Yes' or  'Y' : #ignorable
            attn = True
        elif attn == 'a' or 'A' or 0 or 'Absent' or "n" or 'NO' or 'N' or "no" or 'No' :
            attn = False

        subx[sub] = attn

        # for i in range(sub_to_add):
        att(sub)

    print(subx)
    print("Marked present for",sub,"in data")
    
    
@decorate   #5th
def view_att():
    print(series.to_string())  # to_string will hide dtype and only display data but no data type

    
#===================================
def compare_choice(choiceval):

    if choiceval == 1:  
        cls() 
        today_att()
        ctnue()
        
    elif choiceval == 2:
        # cls()
        print()
        ctnue()

    elif choiceval == 3:
        cls()
        print()
        ctnue()

    elif choiceval == 4:
        cls()
        print()
        ctnue()

    elif choiceval == 5:
        cls()
        view_att()
        print("total attendence :")
        print()
        ctnue()

    elif choiceval == 6:
        cls()
        print()
        ctnue()

    elif choiceval == 7:
        cls()
        print()
        ctnue()

    elif choiceval == 8:
        # cls()
        print()
        ctnue()

    elif choiceval == 9:
        cls()
        print()
        ctnue()

    elif choiceval == 10:
        # cls()
        exit()
        
    else :
        print("Please enter a vaild value")
        ctnue()
        display_menu()
    
while True:
    display_menu()
    choiceval = choice()  # take input and store it 
    compare_choice(choiceval)

# today_att()