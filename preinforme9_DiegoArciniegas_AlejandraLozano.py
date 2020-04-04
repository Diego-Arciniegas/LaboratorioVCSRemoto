# EJERCICIO 1
from math import sqrt

x1 = float(input("ingrase el valor X1:"))
x2 = float(input("ingrase el valor X2:"))
y1 = float(input("ingrase el valor Y1:"))
y2 = float(input("ingrase el valor Y2:"))

total = sqrt((x2-x1)**2 + (y2-y1)**2)

print("Distancia total:",total)

# EJECICIO 2
numero = input("Digite el numero que desee invertirlo:")

def fnInverso(sDato):
    resultado = ""
    PosFinal = len(sDato) - 1
    while (PosFinal >=0):
        resultado = resultado + sDato[PosFinal]
        PosFinal = PosFinal - 1
    return resultado


print("El numero invertido:",fnInverso(numero))

# EJERCICIO 3

# las notas van de 0 a 5
n1 = float(input("ingrase el valor de la nota 1:"))
n2 = float(input("ingrase el valor de la nota 2:"))
n3 = float(input("ingrase el valor de la nota 3:"))
n4 = float(input("ingrase el valor de la nota 4:"))
n5 = float(input("ingrase el valor de la nota 5:"))

total = n1*0.15 + n2*0.20 + n3*0.15 + n4*0.30 + n5*0.20
print("la nota total es:",total)

if total < 2.0 :
    print("El estudiante no puede habilitar")
elif  total < 3.0 :
    print("El estudiante reprobo")
elif  total >= 3.0 :
    print("El estudiante aprobo ")
elif  total > 4.5 :
    print("El estudiante en enhorabuena ha sido uno de los mejores")


# EJERCICIO 4

n= int(input("introduce el numero de renglones:"))
cont = 0
acum = 0
for i in range (n):
    print(acum+cont)
    acum = (acum+cont) * 10 
    cont = cont + 1 