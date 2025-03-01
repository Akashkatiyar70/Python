####String ---- Sequence of charcaters
# s='akash katiyar'
# s1="akash katiyar"
# s8="akash katiyar"


# ### multi-line string written in Doc String
# s2="""akash
# katiyar"""
# s3='''akash katiyar
# hello sir'''

# print(s2,s3,s,s1,s8)



#                                           ## Indexing

# s="python"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])

#                                        #-ve Indexing
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-5])
# print(s[-6])

#                                            ### slicing 
  
# s="python is best" 
# print(s[0:6:1]) 
# print(s[-1:-5:-1])
# print(s[10:14])
# print(s[2:6])

# print(s[:6])



# /                                            SLICING WITH -ve indexing 

# s="python is best" 
# print(s[-14:-8:1]) #access the -ve 
# print(s[0:-8])
# print(s[:-8]) 
# print(s[0:-1])# lets to read starting to end charecters and skip last char
# print(s[1:])  # skip starting first latter and pirint all char
# print(s[: ]) # lets read starting to end
# print(s[:-6])
# print(s[1:-1])



#                               Reverse slicing
# s="python is best" 
# print(s[-1:-5:-1]) # lets count end to start
# print(s[:-5:-1]) # read end to start => tseb
# print(s[::-1]) # this is read it end to start all char like => tseb si nohtyp
# print(s[-1:]) # only read t last char


#                                                      string formatting
# student_name=input("enter student name:")
# course=input("enter course name:")
# start_date=input("Ener Date:")
# batch_name=input("Enter Batch Time:")
#                          1st-type
# Text="hii %s, Your %s batch will start by %s at %s"
# print(Text(student_name,course,start_date,batch_name))

#                          2nd type

# Text="hii {}, Your {} batch will start by {} at {}"
# print(Text.format(student_name,course,start_date,batch_name))

#                           3rd type

# Text=f"hii {student_name}, Your {course} batch will start by {start_date} at {batch_name}"
# print(Text)


#                                                  question ===>11

# s="huhndhsoelmnsjkiiiiiiekkkkkeeeeeeeeeeekkdlllllllls"
# count=[]
# for i in s:
#     count.append(s.count(i))
# print(count)
    
# maxcount=max(count)   
# mincount=min(count)
# print(maxcount,mincount)

# max_index=count.index(maxcount)
# min_index=count.index(mincount)

# print("most frequent letter:",s[max_index])
# print("most frequent letter:",s[min_index])


#                                                    question ===> 9

# s="eye"
# res=s[::-1]
# if res==s:
#     print("palindrome")
# else:
#     print("not palindrome")

#                                                   Question ===> 13

# s="abBHSyBHTSiksjjsjkkkSSS"
# s1=""
# s2=""
# for i in s:
#     if i.islower():
#         s1+=i
#     elif i.isupper():
#         s2+=i
# print(s1+s2)
        
        
        
        
        
        
        
    
##                            ## String methods

# s="aython programs"
# print(s.capitalize()) ##capital first latter in string
# print(s.title())## like capitalize function but every srting first latter capital print
# print(s.upper())


# s="AKASH KATIYAR"
# print(s.lower())
# print(s.casefold()) #give same out put like lower case


# s="Python"
# print(s.swapcase())
# ## print P small latter and all charcters  to print capital

# ##Replace words
# s='python programs'
# print(s.replace("python","java"))



# s="Akash katiyar"
# print(s.split())
## splite data to look aur you give space and splite the data
# s="Akash-katiyar"
# print(s.split('-'))


 
# ## use strip to remove unwanted space starting and last
# s=" pythonbygaudovanrossum "
# print(s)
# s=s.strip()
# input_string=input("Enter Text:")
# if input_string==s:
#     print("matched")
# else:
#     print("Not matched")



# s="Akash katiyar"
# # print(s.count('r'))
# print(s.index('a',8))
# print(s.find('o'))


# s='1'
# print(s.isalpha())
# print(s.isnumeric())
# print(s.isalnum())
# print(s.isdigit())
# print(s.isdecimal())

  
# print(s.isupper())
# print(s.islower())
# print(s.istitle())


##### find out the least and most frequent latters in  string.

# s="aaabbbbbbbcccccbdbfjeeeoejnsnsn"
# count=[]
# for i in s:
#     count.append(s.count(i))
# print(count)
    
# maxcount=max(count)
# mincount=min(count)
# print(maxcount,mincount)

# max_index=count.index(maxcount)
# min_index=count.index(mincount)


# print("Most frequent latter:",s[max_index])
# print("least frequent latter:",s[min_index])





































































