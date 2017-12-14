import re
from pyspark import SparkContext
sc = SparkContext("local", "Simple App")
lines = sc.textFile('C:/Users/Ivgeny/a.txt')
lines_nonempty = lines.filter( lambda x: len(x) > 0 )
print((lines_nonempty.take(1)))