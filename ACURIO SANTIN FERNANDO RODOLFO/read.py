import csv
import time
import chardet
import json
import sys
sys.stdout.encoding
'UTF-8'
c=open('pp.csv', 'rb')
reader = csv.reader(c, delimiter=';')
writer3 = csv.writer(open("codigos.csv", "wb"), delimiter=';')
for index, row in enumerate(reader):
	print row[0].upper()
	cod = chardet.detect(row[0])
	readerp = csv.reader(open('tar.csv', 'rb'), delimiter='\t')
	for index2, row2 in enumerate(readerp):
		if row[0].upper() == row2[1].upper():
			writer3.writerow(row2[0])
