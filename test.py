data = {'math':{"present":0,"absent":0}, 'dsa':{"present":0,"absent":0},'oops':{"present":0,"absent":0},'D.E.':{"present":0,"absent":0}}
sub = input("Enter subject : ") 
attn = str(input("Mark present/absent : ")) #pend logic

list = ['p','P',1,]
#'p' or 'P' or '1' or 'Present' or 'y' or "YES" or 'yes' or 'Yes' or  'Y'
if attn == 1 : #ignorable
    # attn = True
    data[sub]["present"] += 1
elif attn ==  0 :   #dont mix string and number or bool for comparison is 1 and '1' is problem
    # attn = False
    data[sub]["absent"] += 1
    
print(data)