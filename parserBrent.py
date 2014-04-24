# coding=UTF-8
import sys

filename = str(sys.argv[1])

#print filename

#filename = raw_input('檔名：')
 
f = open(filename, 'r')
b_str = f.read()
f.close()
 
#print b_str.decode('utf-8') # 這是什麼？
#print b_str.decode('utf-8').encode('utf-8') # 這是什麼？


index = b_str.find("昨收")
index = index + 36
date = b_str[index:]
date = date[:8]
print 'date=' + date
print 'type=cnyes_Brent'

index = index + 27
price = b_str[index:]
priceIndex = price.find('</td><td class="')
price = price[:priceIndex]
print 'price=' + price