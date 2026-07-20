import pandas as pd
from datetime import datetime
import os 
from opts import decorate,cls,ctnue,dateTime_today,date_today
from layout import display_menu,viewBySubject


##-----------------------------------

data = {'math':{"present":0,"absent":0}, 'dsa':{"present":0,"absent":0},'oops':{"present":0,"absent":0},'D.E.':{"present":0,"absent":0}}
print(data)
# print(data["math"]["present"])  #only for testing
# print(data["dsa"]["absent"])
# print(data["oops"]["absent"])
#---ignore for now deal with only dict 
# series = pd.Series(data)

# print(series.to_string())

#========================================only for pd 

# def inc_sub_attendence(subject):
#     series.loc[subject] += 1

# def att(sub):  #take inc_sunb_attenecence and check if that subject wxit else thorew error
#     try:
#         inc_sub_attendence(sub)
#     except KeyError:
#         print("invailed subject : ",sub)

#+====================================

#---------only attendence----------



def choice(): #subfunc
    try:
        x = int(input())
        # print("working")y
        return x    # pack a choice in variable and call it later for comparison
    except ValueError:
        print("",end='')
#ask ho much lecture today

#menu
    
#================def for options/choice==============================================



#-------------
@decorate  #1st #===========]]]]]]]]]]]]===fix me ==[[[[[[[[[[[[[[]]]]]]]]]]]]]]
def today_att():
    #logic to rmark as absent or present 

    #below only add the attendence by one or add absence by one 
    print("Add today's attendence")
    print("Date : ",end='') 
    date_today()

    sub_to_add = int(input("enter total no. of classes today : "))# take input x time
    if sub_to_add > 8 :
            print("limit exceed : there are only 8 subjects")
    
    #  assume  1 and dry run 

    #empty list
    # subx = {} #not usefull coz now i will update main dict
    for i in range(sub_to_add):
        sub = input("Enter subject : ") 
        attn = str(input("Mark present/absent : ")) #pend logic

        list = ['p','P',1,]
        #'p' or 'P' or '1' or 'Present' or 'y' or "YES" or 'yes' or 'Yes' or  'Y'
        if attn == 1 or attn == '1' or attn == 'P' or attn == 'p' or attn == 'y'or attn == 'Y' or attn == 'Yes' or attn == 'YES' or attn == 'Present' : 
            # attn = True
            data[sub]["present"] += 1
        elif attn == 'a' or attn == 'A' or attn == '0' or attn == 'Absent' or attn == "n" or attn == 0 or attn == 'No'or attn == 'NO'or attn == 'no' :   #dont mix string and number or bool for comparison is 1 and '1' is problem
            # attn = False
            data[sub]["absent"] += 1
#chenge=\\\\\\\\\\\\\\\\\\\\\\\\\\\
        # subx[sub] = attn

        # for i in range(sub_to_add):
        # att(sub)  what it do ??

        # print(subx) #shift tab
        print("sr subject present absent")
        print("1. math   ",data["math"]["present"],'     ',data["math"]["absent"])
        print("2. dsa    ",data["dsa"]["present"],'     ',data["dsa"]["absent"])
        print("3. oops   ",data["oops"]["present"],'     ',data["oops"]["absent"])
        print("4. D.E.   ",data["D.E."]["present"],'     ',data["D.E."]["absent"])
        # print(data)
        print("Marked present for",sub,"in data")
    
    
@decorate   #5th
def view_att():
    # print(series.to_string())  # to_string will hide dtype and only display data but no data type
    print("sr subject present absent")
    print("1. math   ",data["math"]["present"],'     ',data["math"]["absent"])
    print("2. dsa    ",data["dsa"]["present"],'     ',data["dsa"]["absent"])
    print("3. oops   ",data["oops"]["present"],'     ',data["oops"]["absent"])
    print("4. D.E.   ",data["D.E."]["present"],'     ',data["D.E."]["absent"])

#===================================
def compare_choice(choiceval):

    if choiceval == 1:  
        # cls() 
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
        print("================================")
        print("Total attendence ")
        view_att()
        
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
#PENDING 3,4