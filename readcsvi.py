import csv
import time

c=open('tarifario2014.csv', 'rb')
reader = csv.reader(c, delimiter=';')
readerp = csv.reader(open('7126p.csv', 'rb'), delimiter=';')
writer3 = csv.writer(open("codigos.csv", "wb"), delimiter=';')
for index, row in enumerate(reader):
	print row
	for index2, row2 in enumerate(readerp):
		print row2
	writer3.writerow(row)
