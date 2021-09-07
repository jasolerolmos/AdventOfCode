from time import time
start_time = time()
archivo = "day7Input.txt"
luggage = []
total = 0


def Tabs(level):
    for t in range(level):
        print('\t', end='')

def Pantalla(level, texto):
    Tabs(level)
    print(texto)
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

def BuscarEnLuggage(tipoBolsa):
    for bolsa in luggage:
        if bolsa.nombre == tipoBolsa:
            return bolsa



def BuscarHijos(bolsa):
    global total
    algunTrue = False
    if len(bolsa.bolsas) >0:
        for cadaBolsa in bolsa.bolsas:
            if cadaBolsa.nombre == 'shiny gold bag':
                algunTrue = True
            bolsaBuscada = BuscarEnLuggage(cadaBolsa.nombre)
            if len(bolsaBuscada.bolsas)>0:
                #print("Buscar en sus hijos.")
                if BuscarHijos(bolsaBuscada):
                    algunTrue = True
    return algunTrue


def PartOneB():
    f = open(archivo, "r")
    direct = []; diff = set([])
    global total
    
    for line in f:
        line = (line.replace('\n', '')
            .replace('bags', 'bag')
            .replace('no other bag.','')
            .replace('.',''))

        struct = line.split(' contain ')
        bolsa = Bolsa(struct[0])
        
        if len(struct[1])>0:
            for cnt in struct[1].split(', '):
                cantidad = int(cnt.split(' ')[0])
                nombre = cnt.replace(str(cantidad)+' ', '')
                bolsa.bolsas.append(Contenido(nombre, cantidad))
        
        luggage.append(bolsa)

        bolsa = None
    
    eventual = 0
    for cadaBolsa in luggage:
        if BuscarHijos(cadaBolsa):
            eventual=eventual + 1

    return eventual

print("Solución 1:",PartOneB())

#print("Solución 2:",PartTwo())
print("Elapsed time: %0.10f seconds." % (time() - start_time))