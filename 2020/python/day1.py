from time import time

lista = []
f = open("day1Input.txt", "r")
for linea in f:
    lista.append(int(linea.replace('\n', '')))    
f.close()


def Metodo2(lista):
    for a in range(len(lista)):
        for b in range(a, len(lista)):
            for c in range(b, len(lista)):
                if Proceso2(lista[a], lista[c], lista[b]):
                    return True


def Metodo1(lista):
    for num in lista:
        for num2 in lista:
            for num3 in lista:
                if Proceso1(num, num2, num3):
                    return True

def Proceso1(num, num2, num3):
    suma = int(num) + int(num2)
    if (suma==2020):
        print("Encontrados: ", num, " y ", num2)
        print("Solución: ", (int(num)*int(num2)))
        return True

def Proceso2(num, num2, num3):
    suma = int(num) + int(num2) + int(num3)
    if (suma==2020):
        print("Encontrados: ", num, ", ", num2, " y ", num3)
        print("Solución: ", (int(num)*int(num2)*int(num3)))

print("Parte 1")
start_time = time()
Metodo1(lista)
print("Elapsed time: %0.10f seconds." % (time() - start_time))
print("\nParte 2")
start_time = time()
Metodo2(lista)
print("Elapsed time: %0.10f seconds." % (time() - start_time))