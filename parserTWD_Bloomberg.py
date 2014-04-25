# coding=UTF-8
import sys

filename = str(sys.argv[1])
 
f = open(filename, 'r')
b_str = f.read()
f.close()

index = b_str.find('quoteTime') + 20
yy = b_str[index:]
yy = yy[:4]
index += 5
mm = b_str[index:]
mm = mm[:2]
index += 3
dd = b_str[index:]
dd = dd[:2]

print 'date=' + yy + mm + dd
print 'type=bloomberg_USDTWD'

index = b_str.find('Previous Close:') + 35
price = b_str[index:]
price = price[:7]
print "price=" + price;
