import csv
import time
url="78232/"
dias=[2,31,28,31,30,31,30,31,31,30,31,30,31]

for mes in [1,3,4,5,6,7,8,9,10,11,12]:
	print mes
	reader = csv.reader(open(url+'iessENERO.csv', 'rb'), delimiter=';')
	flag=1
	for index, row in enumerate(reader):
		fecha = time.strptime(row[37], "%d/%m/%Y %H:%M")
		if fecha[1]==mes:
			if flag==1:
				writer = csv.writer(open(url+"iess"+str(mes)+".csv", "wb"), delimiter=';')
				flag=2
			writer.writerow(row)
	print "Done!",flag