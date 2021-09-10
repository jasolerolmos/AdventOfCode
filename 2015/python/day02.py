from classes import Solution, Init, CleanLine
day = 2

def AreaGif(gif):
    sizes = [ int(lado) for lado in CleanLine(gif).split("x")]
    sizes.sort()
    caras = list()
    aux = list()

    aux.append(2*sizes[0]*sizes[1])
    aux.append(2*sizes[0]*sizes[2])
    aux.append(2*sizes[1]*sizes[2])

    caras.append(int(sum(aux) + min(aux)/2))
    caras.append(((sizes[0]*2) + (sizes[1]*2)) + (sizes[0]*sizes[1]*sizes[2]))
    
    return caras

def Part1_2():
    [lines, start_time] = Init(day, "1 y 2")
    solucion1 = 0
    solucion2 = 0
    for gif in lines:
        dataGif = AreaGif(gif)
        solucion1 += dataGif[0]
        solucion2 += dataGif[1]
    Solution(solucion1, start_time, 0)
    Solution(solucion2, start_time, 0)


Part1_2()