from time import time
start_time = time()
archivo = "day7Input.txt"

def Tabs(level):
    for t in range(level):
        print('\t', end='')

class Bolsa:
    nombre = ""
    bolsas = []
    def __init__(self, nombre):
        self.nombre = nombre
        self.bolsas = []

def BuscarBolsa(luggage, tipoBolsa):
    for bolsa in luggage:
        for c in bolsa.bolsas:
            if c.nombre.count(tipoBolsa):
                print(c.cantidad,c.nombre)

def SearchDirect(luggage, list):
    direct = []
    for line in luggage:
        for bag in list:
            if line[1].count(bag)>0:
                direct.append(line[0])
    return direct

def SearchInDirect(luggage, list):
    indirect = []
    yes = False
    for line in luggage:
        for bag in list:
            if line[1].count(bag)>0:
                yes = True
        if yes:
            indirect.append(line[0])
            yes = False
    unSet = set(indirect)
    
    return indirect


def PartOne():
    f = open(archivo, "r")
    direct = []; luggage = []; diff = set([])
    for line in f:
        line = line.replace('\n', '')
        line = line.replace('bags', 'bag')
        struct = line.split(' contain ')
        luggage.append(struct)
        contain = struct[1].count('shiny gold bag')
        if contain>0:
            direct.append(struct[0])
        
    direct = SearchDirect(luggage, ['shiny gold bag']);

    lista = []
    lista.append(direct)
    listaTotal = direct 
    anterior =  0
    for i in range(49):
        lista.append(SearchInDirect(luggage, lista[i-1]))
        
        listaTotal = listaTotal + lista[i]
        diff = set(listaTotal)
        if anterior != len(set(listaTotal)):
            anterior = len(diff)
    
    f.close()
    return len(diff)


print("Solución 1:",PartOne())
print("Elapsed time: %0.10f seconds." % (time() - start_time))