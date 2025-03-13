#Se registran temperaturas de 3 ciudades (Quito, Guayaquil y Cuenca) 
#durante una semana (Lunes a Domingo).
#Se deben calcular:
#Promedio de temperatura por ciudad.
#Día más caluroso y más frío por ciudad.
#Temperatura máxima y mínima registrada en la semana.
dias = ["Lunes","Martes","Miercoles", "Jueves", "Viernes","Sabado","Domingo"]
ciudades = ["Quito","Guayaquil","Cuenca"]
temperaturas = [
    #0   1   2
    [15, 28, 12],  #0 Lunes
    [17, 30, 14],  #1 Martes
    [16, 29, 13],  #2 Miércoles
    [18, 31, 15],  #3 Jueves
    [19, 32, 16],  #4 Viernes
    [20, 33, 17],  #5 Sábado
    [21, 34, 18]   #6 Domingo
]

promedioquito = 0
promedioguayaquil = 0
promediocuenca = 0
tempMaxima = 0
tempMinima = 100
diaMasCaluroso = ""
diaMasFrio = ""
ciudadMasCalurosa = ""
ciudadMasFria = ""
for filas in range(len(temperaturas)):
    #promedioquito = promedioquito + temperaturas[filas][0]
    promedioquito += temperaturas[filas][0] #Quito
    promedioguayaquil += temperaturas[filas][1] #Guayaquil
    promediocuenca += temperaturas[filas][2] #Cuencua

print("Los promedios las cuidades son: ")

print(f"El promedio de la ciudad de {ciudades[0]} es {promedioquito/len(temperaturas)}")
print(f"El promedio de la ciudad de {ciudades[1]} es {promedioguayaquil/len(temperaturas)}")
print(f"El promedio de la ciudad de {ciudades[2]} es {promediocuenca/len(temperaturas)}")

print("-"*40)
for ciudad in range(len(ciudades)):
    auxtmpmaxima = temperaturas[0][ciudad]
    auxtmpmimina = temperaturas[0][ciudad]
    auxdiacalor = dias[0]
    diafrio = dias[0]

    for dia in range(len(dias)):
        if temperaturas[dia][ciudad] > auxtmpmaxima:
            auxtmpmaxima = temperaturas[dia][ciudad]
            diaMasCaluroso = dias[dia]
        elif temperaturas[dia][ciudad] < auxtmpmimina:
            auxtmpmimina = temperaturas[dia][ciudad]
            diafrio = dias[dia]
    print(f"El día más caluroso de la ciudad de {ciudades[ciudad]} es {diaMasCaluroso} con {auxtmpmaxima}")
    print(f"El día más frio de la ciudad de {ciudades[ciudad]} es {diafrio} con {auxtmpmimina}")


print("-"*40)

for fila in temperaturas:
    for temp in fila:
        if temp > tempMaxima:
            tempMaxima = temp
        if temp < tempMinima:
            tempMinima = temp
print(f"La temperatura maximo registrada es {tempMaxima}")
print(f"La temperatura minima registrada es {tempMinima}")



#Ejercicio de Practica
#1.- Ordenar los valores de mayor a menor
arreglos = [3, 5, 2, 7, 1, 8, 4, 9, 6]
for i in range(len(arreglos)):
    for j in range(i + 1, len(arreglos)):
        if arreglos[i] < arreglos[j]:
            arreglos[i] = arreglos[j]
            arreglos[j] = arreglos[i]




print(arreglos)