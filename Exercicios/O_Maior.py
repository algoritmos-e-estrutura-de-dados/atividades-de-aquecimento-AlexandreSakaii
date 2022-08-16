a = int(input())
b = int(input())
c = int(input())

maiorAB = (a + b + abs (a - b)) / 2

if maiorAB > c:
    print (maiorAB ,"Eh o maior")
else :
    print (c ,"Eh o maior") 