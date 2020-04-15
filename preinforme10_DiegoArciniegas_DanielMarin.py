import numpy as np

kellogs=np.array([27834,23789,30189,30967,32501,32701,31665,17155,4614,834])
print(kellogs)

# Ejercicio 1
def promedio(prom1,prom2):
        cont = 0
        n = 1
        for i in range(prom1,prom2):
                cont = cont + kellogs[i]
                n += 1
                if (prom1 == 0 and prom2 == 9) :
                        promt = cont/n
                else:
                        promt = (cont+kellogs[prom2])/n
        return promt
def comp(a,b,a2,b2):
        prom1 = promedio(a,b)
        print("Promedio de los 2 primeros años:",prom1)
        prom2 = promedio(a2,b2)
        print("Promedio de los 2 ultimos años:",prom2)
        dif = prom1 - prom2
        return dif
print("La diferencia es :" + str(comp(0,1,8,9)))

# Ejercicio 2
def menors(kellogs):
        menor = kellogs[0]
        long = len(kellogs)
        for i in range(1,long):
                if menor > (kellogs[i]) :
                        menor = kellogs[i]
        return menor
def mayors(kellogs):
        mayor = kellogs[0]
        long = len(kellogs)
        for s in range(1,long):
                if mayor < kellogs[s]:
                        mayor = kellogs[s]
        return mayor
mayor = mayors(kellogs)
menor = menors(kellogs)
def dife(mayor,menor) :
        Dif = mayor - menor
        return Dif
print("Año con la mayor utilidad:",mayor)
print("Año con la menor utilidad:",menor)
print("La diferencia entre la utilidad del año mayor y el menor es: " +str(dife(mayor,menor)))

# Ejercicio 3
def mediana(kellogs):
        k = np.sort(kellogs)
        m = int(len(k))
        if (m%2) == 0 :
                m = (m/2)-1
                p1 = k[int(m)]
                p2 = k[int(m+1)]
                medianaa = (p1 + p2)/2
        else:
                m =(m//2)+1
                medianaa = k[int(m)]
        return medianaa
print("La mediana es: " + str(mediana(kellogs)))

# Ejercicio 4
def compMandM(promedio,mediana):
        media = promedio(0,9)
        medianaa = mediana(kellogs)
        print("La media es " + str(media))
        print("La mediana es " + str(medianaa))
        if media < medianaa :
                M = medianaa - media
                print("Es mayor la mediana con " + str(M))
        else :
                M = media - mediana
                print("La media es mas grande por " + str(M))
print(compMandM(promedio, mediana))

# Ejercicio 5
def Porce(kellogs):
        c = 0
        long = len(kellogs)
        p = 2008
        for r in range(0,long):
                c = c + kellogs[r]
        for m in range(0,long) :
                porap = ((kellogs[m])*100)/c
                print("El porcentaje que aporta el año: " + str(p) + ", es ," + str(porap) + "%.")
                p = int(p) + 1 
print(Porce(kellogs))

# Ejercicio 6
def deficit(kellogs) :
        long = len(kellogs)
        D2017 = kellogs[long-1]
        D2016 = kellogs[long-2]
        deficits = D2016-D2017
        print("El deficit del 2017 comparado con el de el 2016 es de: " + str(deficits) + " cop.")
print(deficit(kellogs))

# putno 7
def defiporcentaje(kellogs) :
        long = len(kellogs)
        A = 2017
        for k in range(0, long-1):
                ult = kellogs[long-1]
                defi = kellogs[long-2] - ult
                defiporce = (defi*100)/ult
                long = long-1
                print("El deficit en porcenta del año: " + str(A) + " ,es, "  + str(round(defiporce,2)) + " %.")
                A = A - 1
print(defiporcentaje(kellogs))

