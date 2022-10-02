import math

x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())

distancia = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))

print("distancia = %1f " %distancia)