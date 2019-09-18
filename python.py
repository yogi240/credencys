#!/usr/bin/python


import sys
#********************IF FUNCTIO EX**********************

var1 = 100
if var1:
   print ("1 - Got a true expression value")
   print (var1)
else:
     print("1-got false")
     print(var1)

var2 = 0
if var2:
   print("2 - Got a true expression value")
   print(var2)
else:
    print("2 got false")
    print(var2)

print ("Good bye!")





#*************SIMPLE FUNCTION EX***************

def main():
    print("hii python")
    
main()




#************SIMPLE FUNCTION EX*******************

def function_name(company="credencys"):
    print("I am working in " + company)
function_name() 
function_name("Fidelity")
function_name("tcs")
function_name("infosys")
 


#****************CAR FUNCTION TASK*********************


def car_rental_cost(days):
    cost = 35 * days
    if days >= 8:
        cost -= 70
    elif days >= 3:
        cost -= 20
    return cost

print(car_rental_cost(7))




#**********EXAMPLE FOR SYS**********


#print(len(sys.argv[0]))
#print(str(sys.argv[2]),"\n",str(sys.argv[3]))




s1="yugandhar"
s2="kodanda"
print(s1+s2)


#**************STRING*****************


a="python"
A="class at evng"
print(a)
print(A)


b="working\"s in cred"
B='Devops\'s eng '
print(b)
print(B)


a ="yogi"
print(a*3)


#r --raw string

print(r'hiii\i am \yogi')
