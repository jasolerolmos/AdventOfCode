from dis import Instruction
from classes import Solution, Init, CleanLine
import numpy as np 

day = 7

mapa = np.zeros((11,11))

listaValores = {}

def Part3():
    [lines, start_time] = Init(day, "1")
    solucion = 0

    lista = {}
    for line in lines:
        line = CleanLine(line)
        #print(f"\n{line}")
        instruction = line.split(" ")
        if len(instruction) == 3:
            lista[instruction[2]] = int(instruction[0])

    for line in lines:
        line = CleanLine(line)
        print(f"\n{line}")
        instruction = line.split(" ")
        
        if len(instruction) == 4:
            #print(f"\t{instruction[0]}")
            a = int(lista[instruction[1]])
            if int(~a) < 0:
                lista[instruction[3]] = 65535 - a
            else:
                lista[instruction[3]] = int(~a)
        elif len(instruction) == 5:
            if instruction[1] == "AND":
                a = int(lista[instruction[0]])
                b = int(lista[instruction[2]])

                lista[instruction[4]] = int(a&b)

            if instruction[1] == "LSHIFT":
                a = int(lista[instruction[0]])
                b = int(instruction[2])
                
                lista[instruction[4]] = int(a<<b)

            if instruction[1] == "RSHIFT":
                a = int(lista[instruction[0]])
                b = int(instruction[2])
                
                lista[instruction[4]] = int(a>>b)
            
            if instruction[1] == "OR":
                a = int(lista[instruction[0]])
                b = int(lista[instruction[2]])
                
                lista[instruction[4]] = int(a|b)

    print("\n\n")
    for v in sorted(lista.items(), key=lambda x: x[0]):
        print(f"{v[0]}: {v[1]}")

    #Solution(solucion, start_time, 0)

def setData(lines):
    lista = {}
    for line in lines:
        line = CleanLine(line)
        instruction = line.split("->")
        lista[instruction[1].strip()] = instruction[0].strip()

    return lista

def is_int(value):
    try:
        a = int(value)
        return True
    except:
        return False

def value(lista, letra):
    global listaValores
    valor = 0

    print(f"\n{letra} => {lista[letra]}")
    
    while(True):
        print(f"Es {lista[letra]} un número? {is_int (lista[letra])}")

        instruction = lista[letra].split(" ")

        if is_int(lista[letra]):
            print(is_int (lista[letra]))            
            valor = np.int16(lista[letra])
            print(f"{letra} {np.int16(valor)}")
            return valor
        else:
            print(f"No es número {lista[letra]}")

            if len(instruction) == 1:
                #print(f"{instruction[0]} vale blabla")
                valor = value(lista, lista[letra])

                listaValores[letra] = valor
                #return int(listaValores[letra])

            elif len(instruction) == 2:
                #print(f"{instruction[1]} Tiene 2 partes, buscando {instruction[1]}")

                if letra not in listaValores:
                    a = value(lista, instruction[1])
                else:
                    a = listaValores[letra]

                #a = int(lista[instruction[1]])
                if int(~a) < 0:
                    valor = 65535 - a
                else:
                    valor = int(~a)
                listaValores[letra] = valor

                #return int(listaValores[letra])

            elif len(instruction) == 3:
                if instruction[1] == "AND":
                    if is_int(instruction[0]):
                        a = int(instruction[0])
                    else:
                        if letra not in listaValores:
                            a = value(lista, instruction[0])
                        else:
                            a = listaValores[letra]        
                    
                    if letra not in listaValores:
                        b = value(lista, instruction[2])
                    else:
                        b = listaValores[letra]
                                           
                    listaValores[letra] = (a&b)

                    print(f"{a} {b} {listaValores[letra]}") 
                
                if instruction[1] == "OR":
                    #print(f"{instruction[1]} Tiene 3 partes, buscando {instruction[0]} y {instruction[2]}")
                    a = value(lista, instruction[0])
                    b = value(lista, instruction[2])

                    if letra not in listaValores:
                        a = value(lista, instruction[0])
                    else:
                        a = listaValores[letra]
                    
                    if letra not in listaValores:
                        b = value(lista, instruction[2])
                    else:
                        b = listaValores[letra]
                                           
                    listaValores[letra] = (a|b)
                    

                if instruction[1] == "LSHIFT":
                    if letra not in listaValores:
                        a = value(lista, instruction[0])
                    else:
                        a = listaValores[letra]

                    b = int(instruction[2])
                    
                    listaValores[letra] = (a<<b)

                    print(f"##############{letra}#######")

                    print(f"{a} {b} {listaValores[letra]}") 

                if instruction[1] == "RSHIFT":
                    if letra not in listaValores:
                        a = value(lista, instruction[0])
                    else:
                        a = listaValores[letra]
                    b = int(instruction[2])
                    
                    listaValores[letra] = (a>>b)
                    
                    print(f"{a} {b} {listaValores[letra]}") 
                
                    print(f"{a} {b} {listaValores[letra]}")

            valor = (listaValores[letra])
            return valor        
            
def Part1():
    [lines, start_time] = Init(day, "1")
    solucion = {}
    global listaValores

    lista = setData(lines)

    for instruction in lista:
        print(f"\n{instruction}")

        operation = lista[instruction].split(" ")
        try:
            if len(operation) == 1:
                listaValores[instruction] = int(operation[0])
                print(f"{instruction} {int(operation[0])}")
        except:
            print(f"", end="")
    
    value(lista, 'a')
    print(listaValores['a'])

    print(len(lista))
    #print(listaValores)

def Part2():
    [lines, start_time] = Init(day, "2")
    solucion = 0

    #Solution(solucion, start_time, 0)

Part1()
#Part2()