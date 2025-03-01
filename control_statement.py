#####Control statement


         ##if block
          ## if else block
          ## if elif block
          ##nested if block
          
          
# n=int(input("Enter any number:"))
# if n>=0:
#     print(n)      #jo indentetion aap pahle decide kane hota h fir agar same block mai agar koi aur print katege tho same indentation  sapace hon chaye    
#     print("+ve value")
#    


# n=int(input("Enter any number:"))
# if n>=0:
#     print(n)
#     print("+ve value")
# else:
#     print("-ve value")
# print("done")    #ye bhi print hoga q ki isme ye indentation space same nahi h tho ye block se bahar h



##Write a program to check eligibity of casting vote.

# age=int(input("Enter your Age:"))
# if age>=18:
#     print("Eligible to cast vote")
# else:
#     print("Not eligible to cast vote")


## write a program to number is even and odd.
# num=int(input("Enter the number:"))
# if num%2==0:
#     print("number is even:",num)
# else:
#     print("number is odd:",num)


#### write a progrem to check elibilty of taking admission in a college
#phy=>65
#chem=>55
#maths>=60

# P,c,m=eval(input("enter the numbers of phy,chem,maths:"))
# if (P>=65):
#     if(c>=55):
#         if(m>=60):
#            print("the candidate is eligible for the college")
#         else:
#             print("The candidate is not eligible")
    
    ## Test
    
# per=int(input("Enter percentage marks:"))

# if per>=60:
#     print("1st division")
# elif per>=45:
#     print("2st division")
# elif per>=33:
#     print("3st division")
# else:
#     print("fail")
    
#                                               ##### Nested if

##write aprogram to check a number a check a +ve number is even or odd

# n=int(input("Enter a number:"))
# if n>0:
#     if n%2==0:
#         print("Even")
#     else:
#         print("odd")
# else:
#         print("number should be +ve")
    
    
#    write a program to check an input character is vowel or consonant

vowel="aeiou"
char=input("Enter the charecter:")    
if char>='a' and char<='z':
    # if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
    if char in vowel:
       print(char,"is vowel")
    else:
       print(char," is consonant")
else:
    print("invalid charcter")
    
    
    
    
    
    


