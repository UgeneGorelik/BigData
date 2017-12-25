# This example will show how to basic map filter reduce functions
#-----------------------------------------------



from functools import reduce

#3 functions add 1, return odd number ,sum

def add(x):
    return  x+1

def odd(x):
    if x%2==1:
        return x

def red(x,y):
    return x+y

#inititate list using map,filter,reduce

a=map(add ,[1,2,3])
b=filter(odd,[1,2,3])
c=reduce(red,[1,2,3])

#inititate list using map,filter,reduce using lambda expression

a1=map(lambda x:x+1,[1,2,3])

b1=filter(lambda x:x%2==1,[1,2,3])

c1=filter(lambda x,y:x+y,[1,2,3])


