from time import time

def BuscarLetra(letra, cadena):
    return cadena.count(letra.replace(':',''))

def isInArray(index, lista): 
    if(lista.count(int(index))>0):
            return True
    return False


def ComprobarClave(letra, cadena, rango):
    lista = []; pos_inicial = -1
    try:
        while True:
            pos_inicial = cadena.index(letra, pos_inicial+1)
            lista.append(pos_inicial+1)
    except ValueError: # cuando ya no se encuentre la letra
        #print(rango[0],'y',rango[1],'=> Posiciones de la letra ',letra,' en la cadena',cadena,':', lista)
        #print(isInArray(rango[0], lista),'y',isInArray(rango[1], lista))
        if(isInArray(rango[0], lista) == isInArray(rango[1], lista)):
            #print("No es válido.")
            return False
        else:
            #print("Es válido.")
            return True
        

def Paso1():
    f = open("day2Input.txt", "r")
    correctas = 0;total=0; solucionPaso2=0
    start_time = time()
    for linea in f:
        total = total+1
        entry = linea.replace('\n', '').split(" ")
        BuscarLetra(entry[1], entry[2])
        cadena = entry[2]; letra = entry[1].replace(':','')
        rango = entry[0].split('-');
        min = rango[0]; max = rango[1]

        veces = BuscarLetra(letra, cadena)  

        if(int(min)<=veces and int(max)>=veces):
            correctas = correctas + 1
            #print('\n',entry[0],'Posiciones de la letra',letra,'en',cadena,'=>',num)
        
    f.close()
    print("Elapsed time: %0.10f seconds." % (time() - start_time))

    print('De las,',total,' entradas, solo',correctas,' son correctas.')

def Paso2():
    f = open("day2Input2.txt", "r")
    total=0; solucionPaso2=0
    start_time = time()
    for linea in f:
        total = total+1
        entry = linea.replace('\n', '').split(" ")
        BuscarLetra(entry[1], entry[2])
        cadena = entry[2]; letra = entry[1].replace(':','')
        rango = entry[0].split('-');
        min = rango[0]; max = rango[1]
        
        if(ComprobarClave(letra, cadena, rango)):
            solucionPaso2 = solucionPaso2 + 1  

    f.close()
    print("Elapsed time: %0.10f seconds." % (time() - start_time))

    print('De las,',total,' entradas, solo',solucionPaso2,' son correctas.')


Paso1()
Paso2()


quit()
start_time = time()

print("Elapsed time: %0.10f seconds." % (time() - start_time))