from libs.functions import *

day = 4

def initTablero():
    tablero = []
    #for c in range(0,5):
    #    tablero.append([])
    return tablero


def TakeTwoList(bitPosition, lines):
    twoList = [[],[]]
    for index in enumerate(lines):
        if lines[index[0]][int(bitPosition)] == "0":
            twoList[0].append(lines[index[0]])
        else:
            twoList[1].append(lines[index[0]])
    return twoList

def Linea(linea):
    for l in linea:
        if int(l) < 1000:
            return False
    return True

def Columna(tablero):
    inlinea = 0
    for c in range(len(tablero)):
        for l in tablero:
            if int(l[c]) < 1000:
                inlinea = 0
                break
            else:
                inlinea += 1
        if inlinea == len(tablero[0]):
            return True
    return False



def Solucion1(tablero):
    solucion = 0
    for lin in tablero:
        for col in lin:
            if int(col) < 1000:
                solucion += int(col)
    return solucion

def Part1():
    [lines, start_time] = Init(day, "1")
    solucion = 0
    
    tableros = []
    tablerosSolucionados = []
    nuevo = initTablero()
    for c in lines[2:]:
        linea = CleanLine(c).replace("  "," ").strip().split(" ");
        #print(f"=> {CleanLine(c)}")
        if len(linea) < 2:
            #print(c)
            if len(nuevo) > 0:
                tableros.append(nuevo)
                #print(nuevo)
            nuevo = initTablero()                
            
        else:
            nuevo.append(linea)
    
    tableros.append(nuevo)

    #print(tableros)
    bombo = CleanLine(lines[0]).split(",")
    #print(f"\n{bombo}")
    def Jugar(bombo, tableros):
        for bola in bombo:
            #print("###############################################")
            #print(bola)
            for idx1, tab  in enumerate(tableros):
                #print("Tablero:", tab,"\n")
                for idx2, lin in enumerate(tab):
                    for idx3, col in enumerate(lin):
                        if col == bola:
                            #print(f"\t{lin} => {bola}", end="")
                            tableros[idx1][idx2][idx3] = 1000 + int(tableros[idx1][idx2][idx3])
                            #print(f" => {lin}")
                    
                    if Linea(lin):
                        return Solucion1(tab)*int(bola)

    
    solucion = Jugar(bombo, tableros)

    Solution(solucion, start_time, 0)

def Part2():
    [lines, start_time] = Init(day, "2")
    solucion = 0
    
    tableros = []
    tablerosSolucionados = []
    nuevo = initTablero()
    for c in lines[2:]:
        linea = CleanLine(c).replace("  "," ").strip().split(" ");
        if len(linea) < 2:
            if len(nuevo) > 0:
                tableros.append(nuevo)
            nuevo = initTablero()                
            
        else:
            nuevo.append(linea)
    
    tableros.append(nuevo)

    bombo = CleanLine(lines[0]).split(",")
    def Jugar(bombo, tableros):
        for bola in bombo:
            for idx1, tab  in enumerate(tableros):
                for idx2, lin in enumerate(tab):
                    for idx3, col in enumerate(lin):
                        if col == bola:
                            tableros[idx1][idx2][idx3] = 1000 + int(tableros[idx1][idx2][idx3])
                    
                    if Linea(tableros[idx1][idx2]) or Columna(tableros[idx1]):
                        if not idx1 in tablerosSolucionados:
                            tablerosSolucionados.append(idx1)
                            
                        if len(tablerosSolucionados) == len(tableros):
                            return Solucion1(tab)*int(bola)
                            
    
    solucion = Jugar(bombo, tableros)

    Solution(solucion, start_time, 0)

Part1()
Part2()