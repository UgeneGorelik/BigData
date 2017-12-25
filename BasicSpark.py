
# This example will show how to basic count lines using Spark
#-----------------------------------------------



import re
from pyspark import SparkContext

#initiate Spark lib  and set context
sc = SparkContext("local", "Simple App")

#map and create dir for words
lines = sc.textFile('C:/Users/Ivgeny/a.txt')


#count nonempty lines
lines_nonempty = lines.filter( lambda x: len(x) > 0 )

#print first row
print((lines_nonempty.take(1)))