import random

N = int(input("Ingrese el número de veces que quiere tirar el dado: "))
I = 1
p = 0

while I <= N:
    numero = random.randint(1 , 6)
    print(str(numero))
    I = I + 1
    if numero == 3:
        p = p + 1

print("El número 3 salio ", str(p), " veces")
