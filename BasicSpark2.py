import re
from pyspark import SparkContext


#initiate Spark lib  and set context

sc = SparkContext("local", "Simple App")

#set file to work on
people = sc.textFile('C:/Users/Ivgeny/a.txt')

#map and create dir for words

p1=people.map(lambda x:x.split('\t'))

#reduce by sum key 3rd field
p2=p1.map(lambda  t : (t[3],1)).reduceByKey(lambda x,y:x+y)

#find min value of 1st and sec field
p3=p1.map(lambda t: (t[1],int(t[2]))).reduceByKey(lambda  x,y,:min(x,y))

print(p3.collect())
