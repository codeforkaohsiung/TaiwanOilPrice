# coding=UTF-8
import sys

filename = str(sys.argv[1])
 
f = open(filename, 'r')
b_str = f.read()
f.close()

index = b_str.find('昨收')
index = index + 36
date = b_str[index:]
date = date[:8]
print 'date=' + date
print 'type=cnyes_Dubai'

index = index + 27
price = b_str[index:]
priceIndex = price.find('</td><td class="')
price = price[:priceIndex]
print 'price=' + price