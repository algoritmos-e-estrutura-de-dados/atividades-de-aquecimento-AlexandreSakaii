import math
a = float(input())
b = float(input())
c = float(input())

areatriangulo = (a * c) / 2
print (f"triângulo = ", areatriangulo)

areacirculo = math.pi * math.pow(c, 2)
print (f"circulo = ", areacirculo)

if (a > b):
    maiorarea = a
    menorarea = b
else:
    maiorarea = b
    menorarea = a

areatrapezio = ((maiorarea + menorarea) * c) / 2
print (f"trapézio = ", areatrapezio)

areaquadrado = math.pow(b, 2)
print (f"Quadrado = ", areaquadrado)

arearetangulo = a * b
print (f"Retângulo = ", arearetangulo)


