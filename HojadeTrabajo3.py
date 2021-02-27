#Ejercicio 1

contraseña = str(input("Ingrese una contraseña: "))

contraseña2 = str(input("Ingrese nuevamente su contraseña: "))

if contraseña == contraseña2:
    print("La contraseña es correcta!")
else: 
    print("La contraseña no coincide :(")


#Ejercicio 2

nombre = str(input("¿Con qué letra incia su nombre?: "))


list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

for i in list:
    if i == nombre:
        i == 0

sexo = str(input("¿Cuál es su sexo? (ingrese 'm' o 'f'): "))

if i == 0 and sexo == 'f':
    print("Usted pertenece al grupo A")
else: 
    print("Usted pertenece al grupo B")