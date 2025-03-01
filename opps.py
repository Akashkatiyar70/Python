####  OOPS  =>  object oriented  programming system

###  Class -->  collection of Functions(methods) and data (attributes)

## type of classes
    
    ## built in class
            ## int,float,list,tuple,set,dict..... etc
    ## user define class


# l=[]
# l.append(9)

# l1=[]
# l1.copy()
# l2=[]  
# l3=list()
# print(type(l))


## A class in python is a user-defined template for creating objects.
## An Object is an instance of a class.
   ## it represents a specific implementation of the class and holds its own data.


##Class attributes
   ##  These are the variables that are shared across all instances of a class. it is defined at the class level,outside any methods.


##Instance attributes
    ##  Variable that are unique to each instance (object) of a class.


###  Methods ==> functions defined into classes

# class Calculator:       ##  Class
#     c=0                 ## c is class Attributes
#     def add(self,a,b):  ## methods   
#         self.a=a        ## a and b are parameters of method
#         self.b=b        ## self.a and self.b are instance attributes
#         return a+b
#     def subtract(self):
#         return self.a-self.b

# obj1=Calculator()      ## obj1,obj2,obj3 are objects of Calculator class
# print(obj1.add(4,7))  ## add(obj1)
# print(obj1.subtract())
# obj2=Calculator()
# obj3=Calculator()



###  Constructor and destructor -default methods to create objects and destroy

# class App:
#     def __init__(self):    ## Constructor always use ==> __init__
#         print("object Created")
#     def __del__(self):     ## destructor always use  ==> __del__
#         print("object destroyed")

# App()


# class Book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#     def View(self):
#         print("Book Title:",self.title)
#         print("Book Author:",self.author)
#         print("Book price:",self.price)

# b1=Book("Python","Akash katiyar",500)

# b1.View()


# class bankaccount:
#     def __init__(self,acc_no,name,balance):
#         self.acc_no=acc_no
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
    
#     def display(self):
#         print("Account no:",self.acc_no)
#         print("Account Holder Name:",self.name)
#         print("Account balance:",self.balance)

# user1=bankaccount(100210505,"Akash katiyar",0)
# user1.deposit(100000)
# user1.display()



# class bankaccount:
#     def __init__(self,acc_no,name,balance):
#         self.acc_no=acc_no
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#     def withdraw(self,amount):
#         self.balance-=amount
#     def bankfee(self):
#         self.balance-=(self.balance*0.05)
#     def display(self):
#         print("Account no:",self.acc_no)
#         print("Account Holder name:",self.name)
#         print("Account balance:",self.balance)

# user1=bankaccount(100210505,"Akash katiyar",0)
# user1.deposit(100000)
# user1.bankfee()
# user1.display()


####  OOPS Features
    ## Inheritance ==> transfer of class properties to another classes
                   ## Single Inheritance
                   ## 
    ## Polymorphism
    ## Encapsulation


# class person:                ###  Parent class
#     def __init__(self,name,location):
#         self.name=name
#         self.location=location
# class Employee(person):      ### child class
#     def display(self):
#         print("Employee Name :",self.name)
#         print("Employee Location :",self.location)
# e1=Employee("akash","Ghaziabad")
# e1.display()



# class person:                ###  Parent class
#     def __init__(self,name,location):
#         self.name=name
#         self.location=location
# class student:
#     def training(self,course):
#         self.course=course
# class Employee(person,student):      ### child class
#     def display(self):
#         print("Employee Name :",self.name)
#         print("Employee Location :",self.location)
#         print("Training-Course",self.course)
# class Manager(Employee):
#     def manager_display(self):
#         self.Expeience=10
#         self.display()
#         print("Total Experience:",self.Expeience )

# # e1=Employee("akash","Ghaziabad")
# # e1.training("Data Science")
# # e1.display()

# m1=Manager("Anuj","kannauj")
# m1.training("Python full stack")
# m1.manager_display()





# class Rectangle:
#     def __init__(self,len,width):
#         self.len=len
#         self.width=width
#     def perimeter           
        
        
###                    ## Encapulation

##instance attribute properties:
    ## public
    ## private
    
# class App:
#     def signup(self,username=None,password=None):
#         if username is not None and password is not None:
#             self.username=username
#             self.__password=password
#             print("User registration sucessfull")
#         else:
#             print("Plase enter valid username and password")
            
#     def Login(self,usrname,pswrd):
#         if self.username==usrname and self.__password==pswrd:
#             print("Login Sucessful")
#         else:
#             print("Login Failed")
#     def reset_password(self,newpassword):
#         self.__password=newpassword   
             
# user=App()
# user.signup("user123",'user@1234')
# user.Login("user123",'user@1234')   

# user.reset_password("user@1234")    

# user.Login("user123",'user@1234')     

# # print(user.username)
# user.username="user1234"
# user.Login("user1234",'user@1234')
# # print(user.__password)
            



##Exception handling


## Exception -- Errors
   #Syntax Error
   #Runtime Errors or Excutional Errors
   
   
# print("Data",10)

# try:
#     i='12'
#     print(i-5)         #TypeError
# except:
#     pass
# print("Ducat")


# try:        
#    n=int(input("Enter a number:"))
#    print("Square:",n**2)
# except:
#     pass

        
        
        
        
        
        
        