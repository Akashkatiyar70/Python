## File handling


##  File --> generic data collection which can be stored permanantly in  memory drive


## File types:
    ##text file  -->  .txt,.doc,.html,.py
    ## Binary files --> image,videos,application

## handling mode:
            ## read  - 'r'
            ## write - 'w'
            ##  append  - 'a'
            ## create  - 'x'


# name=input("Enter User name:")
# f=open("C:/Users/akash/OneDrive/Documents/Desktop/data_python.txt",mode="w")
# open("C:\\Users\\akash\\OneDrive\\Documents\\Desktop\\data_python.txt",mode="x")
# f=open(r"C:\Users\akash\OneDrive\Documents\Desktop\data_python.txt",mode="r")

# f.write(name)
# print(f.read())


# f=open(r"C:\Users\akash\OneDrive\Documents\Desktop\data_python.txt",mode="a")
# # f.write('akash')
# print(f.read())

# f=open("opps.py") ## direct open file
# print(f.read())
 
## Create file direct
# f=open("second.py",'w')
# # print(f.write("hi python"))
# print(f.write("print('hi python')"))

## remove file
# import os
# os.remove("second.py")

## Delete file and folder

# os.rmdir(r'c:\user\ai\Desktop\work_file')

# files=os.listdir(r'c:\user\ai\Desktop\work_file')
# dir=r"r'c:\user\ai\Desktop"


# for i in files:
#     os.remove(os.path.join(dir,i))

# os.rmdir(r'c:\user\ai\Desktop\work_file')

import os
# print(os.path.exists(r'opps.py'))

##   Create folder and delete
# os.mkdir(r"C:\Users\akash\OneDrive\Documents\Desktop\file_handling")
# os.rmdir(r"C:\Users\akash\OneDrive\Documents\Desktop\file_handling")





