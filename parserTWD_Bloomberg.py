# coding=UTF-8
import sys
import sqlite3

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

date = yy + '-' + mm + '-' + dd

print 'date=' + date
print 'type=bloomberg_USDTWD'

index = b_str.find('Previous Close:') + 35
price = b_str[index:]
price = price[:7]
print "price=" + price;

conn = sqlite3.connect('oil_db.sqlite')
c = conn.cursor()
c.execute('SELECT * FROM stocks WHERE time=? and type=?', (date, "bloomberg_USDTWD"))
result = c.fetchone()

if result is None:
	c.execute('INSERT INTO stocks VALUES (?, ?, ?)', (date, "bloomberg_USDTWD", float(price)))
	conn.commit()
else:
	print date + ' bloomberg_USDTWD exist'

c.close()
