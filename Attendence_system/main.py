import pandas as pd
from datetime import datetime
import time
import os 
from opts import decorate,cls,ctnue,dateTime_today,date_today
from layout import display_menu,viewBySubject,AttendancePercentage

data = {'math':{"present":0,"absent":0}, 'dsa':{"present":0,"absent":0},'oops':{"present":0,"absent":0},'D.E.':{"present":0,"absent":0}}
print(data)



def choice(): #subfunc just take a choice and store it in variable , if want to call later again the remove int from here and then where you wanna call , there use it as variable and convert there into int 
    try:
        x = int(input())
        # print("working")y
        return x    # pack a choice in variable and call it later for comparison
    except ValueError:
        print("Input out of scope ",end='')
#ask ho much lecture today
    
#================def for options/choice==============================================

@decorate  
def today_att():
    #logic to mark as absent or present 
    #below only add the attendence by one or add absence by one 
    print("Add today's attendence")
    print("Date : ",end='') ; date_today()

    sub_to_add = int(input("enter total no. of classes today : "))# take input x time
    if sub_to_add > 8 :
            print("limit exceed : there are only 8 subjects")

    for i in range(sub_to_add):
        sub = input("Enter subject : ") 
        attn = str(input("Mark present/absent : ")) #pend logic

        list = ['p','P',1,]
        if attn == 1 or attn == '1' or attn == 'P' or attn == 'p' or attn == 'y'or attn == 'Y' or attn == 'Yes' or attn == 'YES' or attn == 'Present' : 
            data[sub]["present"] += 1
        elif attn == 'a' or attn == 'A' or attn == '0' or attn == 'Absent' or attn == "n" or attn == 0 or attn == 'No'or attn == 'NO'or attn == 'no' :   #dont mix string and number or bool for comparison is 1 and '1' is problem
            data[sub]["absent"] += 1

        print("sr subject present absent")
        print("1. math   ",data["math"]["present"],'     ',data["math"]["absent"])
        print("2. dsa    ",data["dsa"]["present"],'     ',data["dsa"]["absent"])
        print("3. oops   ",data["oops"]["present"],'     ',data["oops"]["absent"])
        print("4. D.E.   ",data["D.E."]["present"],'     ',data["D.E."]["absent"])
        print("Marked present for all given subjects in data")
    
@decorate   #5th
def view_att():
    mp1,ma1 = data['math']['present'] , data['math']['absent']
    dp1,da1 = data['dsa']['present'] , data['dsa']['absent']
    op1,oa1 = data['oops']['present'] , data['oops']['absent']
    Dp1,Da1 = data['D.E.']['present'] , data['D.E.']['absent']

    print("sr subject present absent")
    print(f"2. dsa     {dp1:<5}   {da1}")
    print(f"3. oops    {op1:<5}   {oa1}")
    print(f"1. math    {mp1:<5}   {ma1}") # :7 reserve space by 7 
    print(f"4. D.E.    {Dp1:<5}   {Da1}") # :<5 reserve right space by 5 < for right > for left

#------------logic for percentage --------------------
def percentage():
    total_Mathslecture = data['math']['present'] + data['math']['absent']
    if data['math']['present'] == 0:
        math_percentage = 0 
    else:
        math_percentage = (data['math']['present'] / total_Mathslecture) * 100
    print(math_percentage)


    total_DSAlecture = data['dsa']['present'] + data['dsa']['absent']
    if data['dsa']['present'] == 0:
        dsa_percentage = 0
    else:
        dsa_percentage = (data['dsa']['present'] / total_DSAlecture) * 100
    print(dsa_percentage)


    total_OOPSlecture = data['oops']['present'] + data['oops']['absent']
    if data['oops']['present'] == 0:
        oops_percentage = 0 
    else:
        oops_percentage = (data['oops']['present'] / total_OOPSlecture) * 100
    print(oops_percentage)


    total_DElecture = data['D.E.']['present'] + data['D.E.']['absent']
    if data['D.E.']['present'] == 0:
        DE_percentage = 0 
    else:
        DE_percentage = (data['D.E.']['present'] / total_DElecture ) * 100
    print(DE_percentage)

    mp,ma = data['math']['present'] , data['math']['absent']
    dp,da = data['dsa']['present'] , data['dsa']['absent']
    op,oa = data['oops']['present'] , data['oops']['absent']
    Dp,Da = data['D.E.']['present'] , data['D.E.']['absent']

    total_lectures = mp + ma + dp + da + op + oa + Dp + Da
    overall_presents = mp + dp + op + Dp
    overall_absents = ma + da + oa + Da 
    if overall_presents == 0:
        overall_percentage = 0
    else:
        overall_percentage = (overall_presents/total_lectures) * 100
    print(overall_percentage)
    
    return math_percentage,dsa_percentage,oops_percentage,DE_percentage,overall_percentage
#------------End of logic for percentage----------------------


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
        viewBySubject()
        input()
        ctnue()

    elif choiceval == 4:
        cls()
        a,b,c,d,e = percentage()
        cls()
        AttendancePercentage(a,b,c,d,e)
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
    

if __name__ == "__main__":
    while True:
        display_menu()
        choiceval = choice()  # take input and store it in choiceval ( will be used for comparison )
        compare_choice(choiceval)

#pend = 9,8,7