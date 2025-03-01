## Looping Statement ----to repete(iteration) the execution
##While loop
##for loop

# i=1
# while i<=10:
#     print(i,"Ducat")
#     i=i+1


# i=10
# while i>=1:
#     print(i)
#     i-=1

### write a program to display the multiplication table of a number

# n=5
# i=1
# while i<=10:
#     print(n,'*',i,'=',n*i)
#     i+=1

# n=5
# i=2
# while i<=10:
#     print(n,'*',i,'=',n*i)
#     i+=2
# n=5
# i=1
# while i<=10:
#     print(n,'*',i,'=',n*i)
#     i+=2


# n=5
# i=1
# while i<=10:
#     if i%2==0:  
#          print(n,'*',i,'=',n*i)
#     i+=1




# write a program to run the loop from 1 to 150 display only those values which are divisible by 5 

# num = 1
# while num <= 150:
#     if num % 5 == 0:
#         print(num)
#     num += 1
    
#write a program to display the sum of a series.
    #123456789.............................n


# n=20
# i=5
# s=0
# while i<=n:
#     print(i)
#     s=s+i
#     i+=1
# print("Total sum: ",s)    

# write a program to display the multiplication of a series.
#1,2,3,4,5,6,7,8,9,10

# n=10
# i=1
# s=1
# while i<=n:

#     s=s*i
#     i+=1
# print("Total Multiplication: ",s) 


#write a program to display sum of 10 input numbers.

# i=1
# s=0
# while i<=10:
#     n=int(input("Enter a number:"))
#     s=s+n
#     i+=1
# print("sum:",s)


                                                                    # break statement

# i=1
# while i<10:
#     print(i,"Akash")
#     if i==5:
#         break
#     i+=1



                                                             ####   else block with loop
# Agar ke ek baar bhi kahi pe ruk jata h ya break ho jata h oo ye statement nahi chalta h 
# i=1
# while i<=10:
#     print(i)
#     if i==5:
#         break
#     i+=1
# else:
#     print("Done!")




#Write a program to match the passsword with 3 attempts.





















                                                              ## continue statement
# i=1
# while i<=10:  
#  i+=1
#  if i==3 or i==5 or i==7:
#      continue
#  print(i)


## write a program to display sum of 10 input numbers. Numbers must be +ve
# i=1
# s=0
# while i<=10:
#      i+=1
#      n=int(input("enter a number:"))
#      if n<0:
#          continue 
#      s=s+n
# print("sum:",s)


                                                         ## nested loop
# j=1
# while j<=3:
#     i=1
#     while i<=3:
#         print("i=",i)
#         i+=1
#     j+=1
    
# n=1
# while n<=5:
#     i=1
#     while i<=10:
#         print(n,'*',i,"=",n*i)
#         i+=1
#     n+=1    
    
    

#        write a program to display multiplication table of any number    

# n=5
# for i in range(1,11):
#     print(n*i)

# wtite aprogram to display the sum of a sequnece using for loop

# s=0
# for i in range(1,11):
#     s=s+i
# print("Sum:",s)


                                                   ### break in for loop



# write a program to display the sum of  a 10 input numbers and break the loop if input is -ve numbers
# s=0
# for i in range(1,11):
#     n=int(input("Enter a number:"))
#     if n<0:
#         break
#         s=s+n
# print("sum:",s)


# write a program to display the sum of  a 10 input numbers and skip the loop if input is -ve numbers

# s=0
# for i in range(1,11):
#     n=int(input("Enter a number:"))
#     if n<0:
#         continue
#         s=s+n
# print("sum:",s)


                                                  #### else block in for loop

# for i in range(1,11):
#     print(i)
#     if i==5:
#         break
# else:
#     print("loop execution has completed")
    
    
    
                                             #### nested for loop
# l=[1,2,3,4,5,6,7,8,9]
# for i in l:
#     print(i**2)
    
# l=[[1,2],[3,4],[5,6]]
# s=0
# for i in l:
#     for j in i:
#         # print(j**2)
#         # p=j**2
#         s=s+j
        
# print(s)        
        
                           #####  fabnocci seris   
# a=0
# b=1
# while True:
#     c=a+b
#     if c>50:
#         break
#     print(c)
#     a=b
#     b=c        



####                     for loop
#           
#    for loop ==>  applies on iterables on iterables(str,list,tuple,set dic,range)
   

# i can do value ka squre for loop
# l=[8,3,2,4,5.6,67.6,7.7,66,]
# # l[0]**2
# # l[1]**2
# for i in l:
#     print(i**2)



#### count vowels and consonant not space

# s='akash katiyar is best'
# vowels="aeiouAEIOU"
# v=0
# c=0
# for i in s:
#     if i>='a' and i<='z' or i>='A' and i<='Z':
#        if i in vowels:
#             v+=1
#        else:
#             c+=1
# print("Vowels count:",v)
# print("Consonant count:",c)

 
### write a program to count total numbers of alphabets and digits in as string

# s="abcd12345"
# a=0
# b=0

# for i in s:
#     if i>='a' and i<='z' or i>='A' and i<='Z':
#         a+=1
#     elif i>'0' and i<='9':
#         b+=1
# print("Alphabets count:",a)
# print("Digits count:",b)
        
        
#### iterate for loop from 1 to 10;
# for i in range(1,11):
#      print(i)
     
     
# for i in range (10,0,-1):
#     print(i)



#### write a program to display multiplication table of any number

# n=5
# for i in range(1,11):
#      print(n*i)

    
    
#### write a program to display th sum of a sequnece using for loop
###1,2,3,4,5,6,7,8,9,10
# s=0
# for i in range(1,11):
#     s=s+i
# print("sum:",s)

 
 
### write a program to display the sum of a 10 input numbersand break the loop if -ve numbers
# s=0
# for i in range(1,11):
#     n=int(input("Enter a number:"))
#     if n<0:
#         break
#     s=s+n
# print("Total sum:",s)


### write a program to display the sum of a 10 input numbers and skip the loop if -ve numbers
# s=0
# for i in range(1,11):
#     n=int(input("Enter a number:"))
#     if n<0:
#         continue
#     s=s+n
# print("Total sum:",s)

        
##### else block in for loop
# for i in range(1,11):
#      print(i)
#      if i==5:
#          break
# else:
#     print("loop exection is completed")        
        
        
        
####nested for loop
# l=[1,2,3,4,5]
# for i in l:
#     print(i**2)
        
l=[[1,2],[3,4],[5,6]]

for i in l:
    for j in i:
        print(j**2)











































      