#Ejercicio 1

n = int(input("Ingrese la base y la altura del triángulo, tiene que ser un número entero positivo: "))

for i in range(n): #Delimitar mi rango
    for j in range (i+1):
        print("*", end="")
    print("")

#Ejercicio 2

n1 = int(input("Ingrese un número entero positivo mayor que 2: "))

for j in range(2, n):
    if n1% j == 0:
        break
if (j + 1)  == n:
    print(str(n1) + " es un número primo")
else: 
    print(str(n1) + " no es un número primo")