import csv
import time

mes = [31,28,31,30,31,30,31,31,30,31,30,31]
for x in xrange(1,13):
	c=open('prueba.csv', 'rb')
	reader = csv.reader(c, delimiter=';')
	writer = csv.writer(open("pruebaw"+str(x)+".csv", "wb"), delimiter=';')
	for index,row in enumerate(reader):
		fecha = time.strptime(row[37], "%d/%m/%Y %H:%M")
		if (fecha[1]==x):
			writer.writerow(row)
			print row[31]
