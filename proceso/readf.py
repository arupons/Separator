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
	cod = chardet.detect(row[0])
	if cod['encoding']=='utf-8':
		print 'es utf'
		print cod['encoding'], row[0].decode('utf-8')
	if cod['encoding']=='TIS-620':
		print 'es tis', row[0].decode('TIS-620')
		print cod['encoding']
	if cod['encoding']=='ascii':
		print 'es ascii', row[0].decode('ascii')
		print cod['encoding']
	if cod['encoding']=='ISO-8859-2':
		print 'es ISO-8859-2', row[0].decode('ISO-8859-2')
		print cod['encoding']
	readerp = csv.reader(open('tar.csv', 'rb'), delimiter='\t')
	for index2, row2 in enumerate(readerp):
		if row[0] == row2[1]:
			writer3.writerow(row2[0])
