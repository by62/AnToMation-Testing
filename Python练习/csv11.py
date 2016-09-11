#coding=utf-8
import csv
my_file='D:\\data.csv'
data=csv.reader(file(my_file,'rb'))
for user in data:
    print user[0]
    print user[1]
    print user[2]
    print user[3]
    
