# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 02:16:04 2021

@author: user
"""
# home work 2 
# part 1 testing if the shap that you have is square or not 
length = int ( input ( " please enter the length of the shap you have ")) # take the value of the length of the shap 
breadth = int ( input ( " please enter the breadth of the shap you have ")) # take the value of the breadth of the shap 
if length == breadth :                                                # compar between the length and breadth if they equal 
   print (" the shap you have is a square ")
else :
   print (" the shap you have is not a square ") 
   
   
# part 2 employees bouns
bouns = 0.10  # bouns percent 
salary = int(input(" enter your salary in JD"))    # ask the employe to enter his / her salary
experience_years = int( input( " enter your experience years "))  # ask the employe to enter his / her experience years
if experience_years >= 5 :       # compare  if the years of experence is enough to get a bouns 
   bouns_value = salary * bouns   # the vaule that will add to the main salary 
   salary+= bouns_value           # employe salary after add the bouns value 
   print (" For your great experience and work in our comany we give you a bouns with value " , bouns_value ,"\n AND your  salary will be :" ,salary)
else :
   print (" we sorry you dont have any bouns this year ")
   
   
   
# part 3 absolute value for the numbers 
number = float ( input (" enter any number you want to get the absolut value for it "))   # ask user to enter number 
#absolut_value  
if number <0  : # know if the number is negatine or positive 
    absolute_value= number *-1 
    print ( "the absolute value for the number is " , absolute_value )  # if the number is negative the absolute is multiply the number by mins sign 
else :
    absolute_value= number
    print ( "the absolute value for the number is " , absolute_value )  # if the number is negative the absolute is the number with out any changes
    
    
    
# part 4  age category 
age = float (input ( " enter your age to determine your category "))   # ask to enter the age  and i make it float if the user want to enter  acurate  age years  and months 
if age > 0 and age <14 :      # age range between 0-14 
     category = "Children "
elif  age >= 15 and age <= 24  :    # age range between 15-24
      category = "Youth "
elif  age >= 25 and age <= 64  :    # age range between 25-64
      category = " Adult "      
elif  age >= 65  :      # age range 65 and above 
      category = "Senior"       
       
print ( "your category is " , category ) # print the category after it determined depends on the age range 