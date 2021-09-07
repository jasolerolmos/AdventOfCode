from time import time

def Recorrido1(pasoLateral,bajar):
    f = open("day3Input.txt", "r")
    posX = 0;arboles = 0
    for linea in f:
        linea = linea.replace('\n','')
        if(linea[posX]=="."):
            linea = linea[:posX] + "O" + linea[posX + 1:]

        if(linea[posX]=="#"):
            arboles = arboles + 1
            linea = linea[:posX] + "X" + linea[posX + 1:]

        #print(linea)
        posX = posX + pasoLateral
        if(posX>=len(linea)):
            posX = posX - len(linea)
    
    print('Con',pasoLateral,'Pasamos por',arboles,'árboles.')
    f.close()
    return arboles


def Recorrido2(pasoLateral,bajar):
    f = open("day3Input.txt", "r")
    posX = 1;posY = 0;arboles = 0
    for linea in f:
        linea = linea.replace('\n','')
        if(posY==bajar):
            if(linea[posX]=="."):
                linea = linea[:posX] + "O" + linea[posX + 1:]

            if(linea[posX]=="#"):
                arboles = arboles + 1
                linea = linea[:posX] + "X" + linea[posX + 1:]
                
            posY = 1
            posX = posX + pasoLateral
            if(posX>=len(linea)):
                posX = posX - len(linea)
        else:
            posY = posY + 1
            
        print(linea)
    
    print('Con',pasoLateral,'Pasamos por',arboles,'árboles.')
    f.close()
    return arboles


start_time = time()
pasoLateral = [1, 3, 5, 7]

valores = []
for paso in pasoLateral:
    valores.append(Recorrido1(paso,1))
valores.append(Recorrido2(1,2))

sol = 1
print(valores)
for v in valores:
    sol = sol * v
print("Solución",sol)
print("Elapsed time: %0.10f seconds." % (time() - start_time))
