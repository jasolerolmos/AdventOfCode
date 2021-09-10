from classes import Solution, Init, CleanLine
day = 3

def Part1():
    [lines, start_time] = Init(day, "1")
    solucion1 = list()
    ejeY = 0
    ejeX = 0

    solucion1.append(f"{ejeY} {ejeX}")
    for ruta in lines:
        for direccion in range(len(ruta)):
            if ruta[direccion] == '^':
                ejeY += 1
            elif ruta[direccion] == 'v':
                ejeY -= 1
            elif ruta[direccion] == '<':
                ejeX -= 1
            elif ruta[direccion] == '>':
                ejeX += 1
            
            if f"{ejeY} {ejeX}" not in solucion1:
                solucion1.append(f"{ejeY} {ejeX}")

    Solution(len(solucion1), start_time, 0)

    


Part1()