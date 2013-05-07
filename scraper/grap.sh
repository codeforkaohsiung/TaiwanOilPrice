#!/bin/sh

#Dubai
curl -L http://www.cnyes.com/futures/flashchart/DUBS.html -# -o `date +%Y%m%d`Dubai

#Brent
curl -L http://www.cnyes.com/futures/flashchart/BREN.html -# -o `date +%Y%m%d`Brent

#USDTWD
curl -L http://www.bloomberg.com/quote/USDTWD:CUR -# -o `date +%Y%m%d`USD-TWD
