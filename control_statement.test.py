#                        1. Write a Python program to read the age of a candidate and determine whether it is eligible for casting his/her own vote. 
#                           Test Data : 21
#                           Expected Output :
#                           Congratulation! You are eligible for casting your vote.
  
  
# age=int(input("Enter yours age:"))
# if age>=21:
#     print("Congratulation! You are eligible for casting your vote.")
# else:
#     print("Warning! You are not eligible for casting your vote.")








#                                  2. Write a Python program to read the value of an integer m and display the value of n is 1 when m is larger than 0, 0 when m is 0 and -1 when m is less than 0. 
#                                  Test Data : -5
#                                  Expected Output :
#                                  The value of n = -1

# m=int(input("Enter the value of m:"))
# if m>0:
#     print("1")
# elif m==0:
#     print("0")
# else:
#     print("-1")
    
    
# m=int(input("Enter the Value of m:"))
# if m>0:
#         n=1
# elif m==0:
#         n=0
# else:
#         n=-1
# print(f"The value of n is: {n}")




# Python में f का मतलब है formatted string literals या f-strings। यह एक ऐसी सुविधा है जो Python 3.6 और उसके बाद के संस्करणों में उपलब्ध है।
# f-string का उपयोग
# f के साथ आप string के अंदर variables या expressions को सीधे embed कर सकते हैं। इसे placeholders {} के साथ लिखा जाता है।

# Syntax:python Copy code
# f"Your text {variable_name_or_expression}"
# Example:

# name = "John"
# age = 25
# print(f"My name is {name} and I am {age} years old.")
# Output: My name is John and I am 25 years old.

# n = 10
# print(f"The value of n is: {n}")
# # Output: The value of n is: 10



# x = 5
# y = 10
# print(f"The sum of {x} and {y} is {x + y}.")
# # Output: The sum of 5 and 10 is 15.

# print(f"The square of 4 is {4**2}.")
# # Output: The square of 4 is 16.


#                                               ####Why use f-strings?

# यह अन्य formatting methods (जैसे .format() और % formatting) के मुकाबले आसान और पढ़ने में साफ होता है।
# आप directly expressions और calculations लिख सकते हैं।
# Comparison with .format():

# name = "Alice"
# age = 30

# # Using .format()
# print("My name is {} and I am {} years old.".format(name, age))

# # Using f-string
# print(f"My name is {name} and I am {age} years old.")







# 3. Write a Python program to accept the height of a person in centimeter and categorize the person according to their height. 
# Test Data : 135
# Expected Output :
# The person is Dwarf.
# <140   Dwarf
# <140  >170 Average
# >170    Tall

# h=float(input("Enter the your height:"))
# if h < 140:
#     c="Dwarf"
# elif 140 <= h <=170:
#     c="Average"
# else:
#     c="Tall"
# print(f"The person is:{c}.")


# h=float(input("Enter the height of the person in centimeters:"))

# if h<140:
#     print("The person is Dwarf")
# elif 140 <=h<=170:
#     print("The person is Average")
# else:
#     print("The person is Tall")



# 4. Write a Python program to find the largest of three numbers. 
# Test Data : 12 25 52
# Expected Output :
# 1st Number = 12,        2nd Number = 25,        3rd Number = 52
# The 3rd Number is the greatest among three




# a,b,c=eval(input("enter the numbers:"))
# print(f"1st Number = {a},    2nd Number = {b},           3rd Number = {c}")
# if a >b and a >c:
#     l = "1st"
#     g = a
# elif b > a and b > c:
#     l = "2nd"
#     g = b
# else:
#     l= "3rd"
#     g = c
# print(f"The {l} Number is the greatest among three: {g}")



# n1=int(input("Enter a number:"))
# n2=int(input("Enter second number:"))
# n3=int(input("Enter third number:"))
# if n1>n2 and n1>n3:
#     print(n1,"is largest")
# elif n2>n1 and n2>n3:
#     print(n2,"is largest")
# else:
#     print(n3,"is largeast")




# 5. Write a Python program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies. 
# Test Data : 7 9
# Expected Output :
# The coordinate point (7,9) lies in the First quadrant.



# def num(x,y):
#     if x>0 and  y>0:
#         return "First quadrant"
#     elif x<0 and y>0:
#         return "Second quadrant"
#     elif x<0 and y<0:
#         return "Third quadrant"
#     elif x>0 and y<0:
#         return "Fourth quadrant"
#     elif x==0 and y==0:
#         return " at the origin"
#     elif x==0:
#         return "On the y axis"
#     elif y==0:
#         return "On the x-axis"
    
# x=int(input("Enter the x coordinates: "))
# y=int(input("Enter the y coordinates: "))
    
# quadrant = num(x, y)
    
# print(f"The coordinates point({x},{y}) lies {quadrant}.")





# def find_quadrant(x, y):
#     if x > 0 and y > 0:
#         return "First quadrant"
#     elif x < 0 and y > 0:
#         return "Second quadrant"
#     elif x < 0 and y < 0:
#         return "Third quadrant"
#     elif x > 0 and y < 0:
#         return "Fourth quadrant"
#     elif x == 0 and y == 0:
#         return "at the Origin"
#     elif x == 0:
#         return "on the Y-axis"
#     elif y == 0:
#         return "on the X-axis"

# # Accepting input
# x = int(input("Enter the X coordinate: "))
# y = int(input("Enter the Y coordinate: "))

# # Determining the quadrant
# quadrant = find_quadrant(x, y)

# # Outputting the result
# print(f"The coordinate point ({x},{y}) lies {quadrant}.")

#     6. Write a Python program to find the eligibility of admission for a professional course based on the following criteria: 
# Eligibility Criteria : Marks in Maths >=65 and Marks in Phy >=55 and Marks in Chem>=50 and Total in all three subject >=190 or Total in Maths and Physics >=140 ------------------------------------- 

# math,phy,chem=eval(input("Enter the marks:"))
# marks=math+phy+chem
# num=math+phy
# if math>=65 and phy>=55 and chem>=50:
#     print("the numbers",math,phy,chem)
# elif marks>=190 or num>=140:
#     print("Eligibility to in exam")
    



# 7. Write a Python program to calculate the root of a Quadratic Equation. 
# Test Data : 1 5 7
# Expected Output :
# Root are imaginary;
# No solution.
# ax^2+bx+c=0

# a=5
# b=9
# c=3
# d= b**2 -4*a*c
# root1= ((-b)+d**0.5)/(2*a)
# root2= ((-b)-d**0.5)/(2*a)

# print(root1)
# print(root2)

# if d<0:
#     print("roots are imaginary")
# elif d==0:
#     print("root are real and same")
# elif d>0:
#     print("roots are real and differtnt")


    