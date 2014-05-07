# coding=UTF-8
import sys
import sqlite3

filename = str(sys.argv[1])
 
f = open(filename, 'r')
b_str = f.read()
f.close()

index = b_str.find('昨收')
index += 36

yy = b_str[index:]
yy = yy[:4]
index += 4
mm = b_str[index:]
mm = mm[:2]
index += 2
dd = b_str[index:]
dd = dd[:2]
date = yy + '-' + mm + '-' + dd

print 'date=' + date
print 'type=cnyes_Dubai'

index += 21
price = b_str[index:]
priceIndex = price.find('</td><td class="')
price = price[:priceIndex]
print 'price=' + price

conn = sqlite3.connect('oil_db.sqlite')
c = conn.cursor()
c.execute('SELECT * FROM stocks WHERE time=? and type=?', (date, "cnyes_Dubai"))
result = c.fetchone()

if result is None:
	c.execute('INSERT INTO stocks VALUES (?, ?, ?)', (date, "cnyes_Dubai", float(price)))
	conn.commit()
else:
	print date + ' cnyes_Dubai exist'

c.close()