import csv
import time

c=open('iessdic.csv', 'rb')
reader = csv.reader(c, delimiter=';')
writer01 = csv.writer(open("iess01.csv", "wb"), delimiter=';')
writer02 = csv.writer(open("iess02.csv", "wb"), delimiter=';')
writer03 = csv.writer(open("iess03.csv", "wb"), delimiter=';')
writer04 = csv.writer(open("iess04.csv", "wb"), delimiter=';')
writer05 = csv.writer(open("iess05.csv", "wb"), delimiter=';')
writer06 = csv.writer(open("iess06.csv", "wb"), delimiter=';')
writer07 = csv.writer(open("iess07.csv", "wb"), delimiter=';')
writer08 = csv.writer(open("iess08.csv", "wb"), delimiter=';')
writer09 = csv.writer(open("iess09.csv", "wb"), delimiter=';')
writer10 = csv.writer(open("iess10.csv", "wb"), delimiter=';')
writer11 = csv.writer(open("iess11.csv", "wb"), delimiter=';')
writer12 = csv.writer(open("iess12.csv", "wb"), delimiter=';')

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
