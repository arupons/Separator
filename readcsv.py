import csv
import time

c=open('prueba.csv', 'rb')
reader = csv.reader(c, delimiter=';')
writer2 = csv.writer(open("pruebaw2.csv", "wb"), delimiter=';')
writer3 = csv.writer(open("pruebaw3.csv", "wb"), delimiter=';')
tmp2 = []
tmp3 = []
cont3 = 0
cont2 = 0
for index, row in enumerate(reader):
    fecha = time.strptime(row[37], "%d/%m/%Y %H:%M")
    if (fecha[1]==2):
        cont2=cont2+1;
        print "Febrero",str(cont2)," ",row
        writer2.writerow(row)
        tmp2.append(row)
    elif(fecha[1]==3):
        cont3=cont3+1
        print "Marzo"+str(cont3)
        writer3.writerow(row)
        tmp3.append(row)

    #writer2.writerow(tmp2)
    #writer3.writerows(tmp3)
