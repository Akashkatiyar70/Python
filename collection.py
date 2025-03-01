### List
### list is a collection whwere we can collect any type of data
### list is an indexed collection
### list is mutable coolection
### duplicate elements can be stored in list

###Tuple
### Tuple is a collection whwere we cwn collect any type of data
### Tuple is an indexed collection
### Tuple is  inmutable coolection
### duplicate elements can be stored in tuple


###Set
### set is a collection whwere we can collect any type of data except data
### set is an unindexed collection
### set is mutable coolection
### duplicate elements cannot be stored in list

### dict
### dict is a collection whwere we cwn collect data in keys and value
### dict is an indexed collection by keys
### dict is mutable coolection
### duplicate elements can be stored in dict values but keys cannot.


# li =[34,"Python",23.87,True,"Python"]
# print(li)
# print(li[1])
# print(li[2])

# print(len(li))
# print(li[-1])



# ## Slicing
# li =[34,"Python",23.87,True,"Pythonnn"]
# # print(li[:3])

# # print(li[2:])
# print(li[-3:])
# print(li[1:-1])

###Function on list

# li=[1,2,3,44,5,6,77,66,7,8,9,0,99,00,12]
# # li=['a','b','c','e','d','z','W']

# print(len(li))
# print(max(li))
# print(min(li))
# print(sum(li))
# print(sorted(li))
# print(sorted(li,reverse=True))
# print(li)

#                  ###update the value into list

# li =[34,"Python",23.87,True,"Pythonnn"]
# li[1]="java"
# print(li)


# #               multiple index value data change and update
# li =[34,"Python",23.87,True,"Pythonnn"]

# li[1:3]="Data science","akash katiyar",34
# print(li)


# ## list method
# l=[34,'akash','python',21.4]

# l.append(True) #append means last mai data ko add karna
# print(l)

# l.insert(0,'data science')

# ##Add multiple data use ==> extend([])
# l.extend([1,2,3,4,5,6])

# l.remove("python")

# l.remove(l[2]) # remove use index
# l.pop(3)

# print(l)

# ## Write a python progra that takes two lists and returns Ture if they have a
# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10,3]
# for i in l1:
#     if i in l2:
#         print(True)
#         break
# else:
#     print(False)


## Write a python program to generate a 3*4*6 3D array whose ech element is
#[*,*,*,*,*,*,*,*]  1D array
#[[*,*,*,*,*,*,*,*],
# [*,*,*,*,*,*,*,*],
# [*,*,*,*,*,*,*,*],
# [*,*,*,*,*,*,*,*]] #4*8


##3D collection of 2D
#[[[*,*,*,*,*,*,*,*],
# [*,*,*,*,*,*,*,*],
# [*,*,*,*,*,*,*,*],
# [*,*,*,*,*,*,*,*]] 
#[[*,*,*,*,*,*,*,*],
# [*,*,*,*,*,*,*,*],
# [*,*,*,*,*,*,*,*],
# [*,*,*,*,*,*,*,*]] 
# [[*,*,*,*,*,*,*,*],
# [*,*,*,*,*,*,*,*],
# [*,*,*,*,*,*,*,*],
# [*,*,*,*,*,*,*,*]] ## 3*4*8]


###    1D Array

# li=[]
# for i in range(6):
#      li.append('*')
# print(li)


#####   2D Array


# l2=[]
# for j in range(4):  
#    l1=[]
#    for i in range(6):
#      l1.append('*')
#      l2.append(l1)
# print(l2)



#### 3D Array

# l3=[]
# for k in range(3):
#     l2=[]
#     for j in range(4):  
#          l1=[]
#          for i in range(6):
#             l1.append('*')
#          l2.append(l1)
#     l3.append(l2)     
# print(l3)



###    Tuple

# t=(1,2,4,5,6,"python",True,"python")
# print(t)

## Indexing 

# print(t[0])
# print(t[1])
# print(t[2])

## -ve indexing

# print(t[-1])
# print(t[-2])

# ## slicing
# print(t[1:3])
# print(t[3:])


### function on tuple 

# print(len(t))
# print(max(t))
# print(min(t))
# print(sum(t))
# print(sorted(t))

# ## Tuple methods
# t=(1,2,4,5,6,"python",True,"python")

# print(t.count("python"))

# print(t.index("python"))



##     Packing and Unpacking

##  Packing
# a=1
# b=2,3,4,5,6,7 # by default make Tuple ==> (2, 3, 4, 5, 6, 7)
# print(b)


# ##   Unpacking

# a,b,c=3,4,5
# print(a)
# print(b)
# print(c)


# t=(4,)
# print(type(t))


# ### Set

# t={3,"python",(1,2,3),"python",34,True}
# print(t)

# print(len(t))
# # print(max(t))
# # print(min(t))
# # print(sum(t))
# # print(sorted(t))

# for i in t:
#     print(i)


# ####              set Add methods
# s={3,"python",(1,2,3),"python",34,True}
# s.add(46)
# print(s)
# s.update([3,2,4,67.6,65.356,4544545])
# print(s)

# s.remove("python") ## not match data and throw the error
# print(s)

# # s.remove("python")
# # s.discard("python") ## not match data and not throw the error
# print(s)

# s.pop()  ## remove random data not give any value
# print(s) 

# s.clear()
# print(s)

###    Print Intersection value in set

# s={3,"python",(1,2,3),"python",34,True}
# s1={3,"python","Ducat",34,18,False}
# s2={3,"python",(1,2,3),"python"}
# s4={13,"msdkkjdj",564,56,87,}
# s5={3,"python",(1,2,3),"python",34,True}

# print (s.intersection(s1))
# print(s.union(s1))
# print(s.difference(s1))
# print(s.symmetric_difference(s1))
# print(s.issuperset(s2))
# print(s2.issubset(s))

# print(s.isdisjoint(s2))
# print(s.isdisjoint(s1))
# print(s.isdisjoint(s4))
# print(s.isdisjoint(s5))



########              Dictionary (dict)
# d={'name':'Akash',1:True,False:0,1:'One'}

# print(1 in d.keys())
# print(d)

# print(d['name'])
# print(d[1])
# print(d[False])

###  Looping with dict

# for i in d:
#     print(i)

# for i in d.values():
#     print(i)

# for i,j in d.items():
#     print(i,j)



# ####      Dict Methods

# d={'name':'Akash',1:True,False:0,1:'One'}

# ## update single value and keys
# d.setdefault('Address',"Ghaziabad")
# print(d)


# # update multiple value and keys
# d.update({"Age":18,"course":"Java"})
# print(d)


# ##use pop and remove keys
# d.pop(1)
# print(d)

# ### use popitem and remove dict last items
# d.popitem()
# print(d)


# # d.clear()
# # print(d)

# print(d.get('name'))


# print(d.keys())
# print(d.values())
# print(d.items())

















































































































































































































