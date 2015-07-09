import csv
import time

c=open('tarifario20142.csv', 'rb')
reader = csv.reader(c, delimiter=',')
readerp = csv.reader(open('7126p.csv', 'rb'), delimiter=';')
writer3 = csv.writer(open("codigos.csv", "wb"), delimiter=';')
for index2, row2 in enumerate(reader):
	print row2[2]
