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
