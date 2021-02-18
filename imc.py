
print("Bienvenido a la Hoja de Trabajo 0")
print("Esta es una calculadora del Índice de masa corporal")
print("----------------------------------------------------")
peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu altura en metros? ")
imc = round(float(peso)/float(estatura)**2,2)
print("----------------------------------------------------")
print("Tu índice de masa corporal es: " + str(imc))