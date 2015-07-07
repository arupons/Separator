import csv
import time

c=open('iessmarzo.csv', 'rb')
reader = csv.reader(c, delimiter=';')

for index, row in enumerate(reader):
    fecha = time.strptime(row[37], "%d/%m/%Y %H:%M")
    if fecha[1]==1:
        writer01.writerow(row)
    elif fecha[1]==2:
        writer02.writerow(row)
    elif fecha[1]==3:
        writer03.writerow(row)
    elif fecha[1]==4:
        writer04.writerow(row)
    elif fecha[1]==5:
        writer05.writerow(row)
    elif fecha[1]==6:
        writer06.writerow(row)
    elif fecha[1]==7:
        writer07.writerow(row)
    elif fecha[1]==8:
        writer08.writerow(row)
    elif fecha[1]==9:
        writer09.writerow(row)
    elif fecha[1]==10:
        writer10.writerow(row)
    elif fecha[1]==11:
        writer11.writerow(row)
    elif fecha[1]==12:
        writer12.writerow(row)
