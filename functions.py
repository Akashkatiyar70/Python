## Functions --> is a process storage


## function types:
            ## built in functions
                ## print,input,sum,max,min,len .....etc
            ## user defined functions

## step to use function

   ## define the process
   ### calling the function
   
   
###   syntex to define the function

# def function_name(parameters(Optional)): 
#     process_statement or pass 
#     return value (Optional)
    
# def display():
#     print("Ducat")     
    
# display()
# display()
# display()
# display()


## write a function to display multiplication table of a number

# def multiplication_table():
#     n=5
#     for i in range(1,11):
#         print(n,'*',i,'=',n*i)
        
# multiplication_table()
# multiplication_table()


# def multiplication_table(n):
#     # n=5
#     for i in range(1,11):
#         print(n,'*',i,'=',n*i)

# multiplication_table(8)
# multiplication_table(7)


### write a function to check any number is even or odd

# def even_odd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
        
# even_odd(2)
# even_odd(3)
    

###  Write a function to define to check any collection is empty or not.
    

# def check_empty(col):
#     if len(col)==0:
#         print("Empty")
#     else:
#         print("Not Empty")
        
# check_empty([6])
# check_empty([])
        
        
# def multiply(n1=1,n2=1):  ## n1 and n2 parameters
#     m=n1*n2
#     print("Multiplication:",m)
    
    
# multiply(3,4) ## arguments values  (these arguments values pass parameters(like= n1,n2))
# multiply(2,8)
# multiply(2) #TypeError: multiply() missing 1 required positional argument: 'n2'
# multiply(3,4,5) ##TypeError: multiply() takes 2 positional arguments but 3 were given

# multiply(2)

# multiply(n2=6) ## Keyword argument



# def customer_details(name,contact,country):
# def customer_details(name="Guest",contact=None,country="India"):
#     print("Customers Name:",name)
#     print("Contact:",contact)
#     print("Country:",country)
    
# # customer_details("Akash",8318977670,"India")
# customer_details()



# def multiply(n1=1,n2=1):  ## n1 and n2 parameters
#     global m
#     m=n1*n2
#     print("Multiplication:",m)
    
# multiply()
# print(m)



# def multiply(n1=1,n2=1):  ## n1 and n2 parameters
#     m=n1*n2
#     return m

# print(multiply())
# print(multiply(5,6))


###   Write a function to return true and false if number is prime or not



# def isprime(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         return True
#     else:
#         return False

# print(isprime(7)) 


# def factorial(n):
#     m=1
#     for i in range(n,0,-1):
#         m*=i
#     return m
# print(factorial(5))



## write a python function that takes a list 
# add returns a new list with unique elements of the first list.
#[1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
# def unique_list(l):
#     li=[]
#     for i in l:
#         if i not in li:
#             li.append(i)
#     return li
# l2=unique_list([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6])
# print(l2)




































































