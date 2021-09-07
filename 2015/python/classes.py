from time import time
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ClonarLista(program):
    temp = list()
    for p in program:
        temp.append(Instruccion(p.tipo, p.valor))

    return temp



class Instruccion():
    tipo = ""
    valor = 0
    used = False
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.used = False

class Bolsa:
    nombre = ""
    bolsas = []
    def __init__(self, nombre):
        self.nombre = nombre
        self.bolsas = []

class Contenido:
    cantidad=0
    nombre=""
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

def getLines(filename):
    f = open("../input/"+filename, 'r')
    lines = f.readlines()
    f.close()
    return lines

def Init(day, part):
    if len(sys.argv) > 1 and sys.argv[1]=='test':
        archivo = "test"+str(day).rjust(2,"0")+".txt"
    else:
        archivo = "input"+str(day).rjust(2,"0")+".txt"

    print(f"\nParte {part}\n")
    return [getLines(archivo), time()]

def Solution(solucion, start_time, loops):
    print(f"Solution: {solucion}\t\tElapsed time: {time() - start_time} seconds. Loops: {loops}",end='\n')

def msgTiempo(minuto, start_time, saltoTiempo):
    print(f"{bcolors.OKCYAN}", end='')
    print(' {:>20}'.format(minuto), end='')
    print(f"{bcolors.ENDC}", end='')
    print(f"\n\t\tSalto: {time() - saltoTiempo}" + f"\n\t\tTotal: {(time() -start_time)}", end='\n')

def CleanLine(cadena):
    return cadena.replace('\n', '').replace('\r', '')


def CopyArray(orig):
    dest = []
    for idxRow, row in enumerate(orig):
        empty = []
        for idxCol, col in enumerate(row):
            empty.append(orig[idxRow][idxCol])
        dest.append(empty)
    return dest