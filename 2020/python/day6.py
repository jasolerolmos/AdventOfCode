from time import time
import urllib.request

start_time = time()

#f = open("ejemplo.txt", "r")


def AnalizarGrupo(respuestas):
    yes = 0;
    for rsp in range(ord('a'), ord('z')+1):
        n = respuestas.count(chr(rsp));
        if(n>0):
            yes = yes + 1
            #print(chr(rsp),': ',n)
    return yes

def AnalizarGrupo2(group):
    #print('\n\n',group)
    yes = 0;
    for rsp in range(ord('a'), ord('z')+1):
        n = 0;
        for person in group:
            if chr(rsp) in person:
                n = n + 1
        #if n>0:
            #print('La letra ',chr(rsp),' la tienen: ', n,'de',len(group))
        if n == len(group):
            yes = yes + 1
    return yes


def PartOne():
    sol1 = 0
    f = open("day6Input.txt", "r")
    listaGrupos = []
    grupo = ""
    total=0
    for linea in f:
        linea = linea.replace('\n', '')
        if(len(linea)>0):
            grupo = grupo + linea
        else:
            total = total + 1
            grupo = grupo.strip()
            listaGrupos.append(grupo)
            yes = AnalizarGrupo(grupo)
            sol1 = sol1 + yes
            grupo = ''

    f.close();
    return sol1

def PartTwo():
    sol1 = 0
    f = open("day6Input.txt", "r")
    groupList = []
    group = []
    total=0
    for line in f:
        line = line.replace('\n', '')
        if(len(line)>0):
            group.append(line)
        else:
            total = total + 1
            groupList.append(group)
            yes = AnalizarGrupo2(group)
            sol1 = sol1 + yes
            #print(group,': ',yes)
            group = []

    f.close();
    return sol1



print("Solución 1:",PartOne())
print("Solución 1:",PartTwo())
print("Elapsed time: %0.10f seconds." % (time() - start_time))