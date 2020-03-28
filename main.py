from math import sqrt

a = int(input("ingrase el primer valor:"))
b = int(input("ingrase el primer valor:"))
c = int(input("ingrase el primer valor:"))
d=((b**2)-4*a*c)

if ((b**2)-4*a*c) > 0:
    x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
    print("Los valores de x son:")
    print("valor de x1:",x1)
    print("valor de x2:",x2)
elif ((b**2)-4*a*c) == 0:
    z = (-b/(2*a))
    print("x1 y x2 son iguales y corresponden:",z)
elif ((b**2)-4*a*c) < 0:
    print("no se puede resolver la ecuacion")

