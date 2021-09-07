from time import time
import classes

start_time = time()
archivo = "day8Input.txt"
#archivo = "test.txt"

class Instruccion():
    tipo = ""
    valor = 0
    used = False
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.used = False

def ExecuteProgram(program):
    Doble = False
    accumulator = 0
    numInstruction = 0
    while (not Doble and numInstruction != len(program)):
        actual = program[numInstruction]
        if not actual.used:
            if actual.tipo == "nop":
                numInstruction = numInstruction + 1
                actual.used = True
            else:
                if actual.tipo == "acc":
                    accumulator = accumulator + int(actual.valor)
                    numInstruction = numInstruction + 1
                    actual.used = True
                else:
                    if actual.tipo == "jmp":
                        numInstruction = numInstruction + int(actual.valor)
                        actual.used = True
        else:
            Doble = True
            return [False, accumulator]

        if numInstruction >= len(program):
            Doble = True

    return [True, accumulator]

def ClonarPrograma(program):
    temp = list()
    for p in program:
        temp.append(Instruccion(p.tipo, p.valor))

    return temp

def PartOne():
    f = open(archivo, "r")
    program = []
    for line in f:
        line = line.replace('\n', '').replace('\r', '')
        if len(line) > 2:
            app = line.split(' ')
            program.append(Instruccion(app[0], app[1]))

    return ExecuteProgram(program)[1]

def PartTwo():
    f = open(archivo, "r")
    program = []
    for line in f:
        line = line.replace('\n', '').replace('\r', '')
        if len(line) > 2:
            app = line.split(' ')
            program.append(Instruccion(app[0], app[1]))

    for num, line in enumerate(program, start=0):
        fixed = ClonarPrograma(program)
        if line.tipo == "nop":
            fixed[num] = Instruccion("jmp", line.valor)
                
        if line.tipo == "jmp":
            fixed[num] = Instruccion("nop", line.valor)

        resultado = ExecuteProgram(fixed)
        if resultado[0]:
            return resultado[1]

    return 0


print(f"{classes.bcolors.OKBLUE}Solución 1:",f"{classes.bcolors.OKGREEN}",PartOne(),f"{classes.bcolors.ENDC}")
print("Elapsed time: %0.10f seconds." % (time() - start_time))
start_time = time()
print(f"{classes.bcolors.OKBLUE}Solución 2:",f"{classes.bcolors.OKGREEN}",PartTwo(),f"{classes.bcolors.ENDC}")
print("Elapsed time: %0.10f seconds." % (time() - start_time))

