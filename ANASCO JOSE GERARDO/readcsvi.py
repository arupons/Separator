import csv
import time

c=open('tarifario20143.csv', 'rb')
reader = csv.reader(c, delimiter=',')
writer3 = csv.writer(open("codigos.csv", "wb"), delimiter=';')
for index, row in enumerate(reader):
	readerp = csv.reader(open('7126p.csv', 'rb'), delimiter=';')
	for index2, row2 in enumerate(readerp):
		print index2," ",row[1].encode ('ISO8859-1'),index2," ","",index2," ",row2[0]
		if row[1] == row2[0]:
			print row2
			writer3.writerow(row2)
