from libs.functions import *

day = 3


def TakeTwoList(bitPosition, lines):
    twoList = [[],[]]
    for index in enumerate(lines):
        if lines[index[0]][int(bitPosition)] == "0":
            twoList[0].append(lines[index[0]])
        else:
            twoList[1].append(lines[index[0]])
    return twoList

def Part1():
    [lines, start_time] = Init(day, "1")
    solucion = 0
    position = [0,0]
    bits = []
    lenth = len(CleanLine(lines[0]))
    for i in range(lenth):
        bits.append([0,0])
    
    print(bits)
    print("\n########################\n")
    for c in range(0, len(lines)):
        line = CleanLine(lines[c])
        

        for index, l in enumerate(line):
            print(l, end=" => ")
            if l == "0":
                bits[index][0] += 1
            else:
                bits[index][1] += 1
        print(line)
        print(bits)
        print("")
    
    print(bits)
    solucion = position[0] * position[1]

    cad0 = ""
    cad1 = ""
    for index in range(lenth):
        if bits[index][0] > bits[index][1]:
            cad0 += "1"
            cad1 += "0"
            print("0", end="")
        else:
            cad0 += "0"
            cad1 += "1"
            print("1", end="")

    print(f"\n{cad0} --- {cad1}")
    print(f"\n{int(cad0,2)} --- {int(cad1,2)}")
    solucion = int(cad0,2) * int(cad1,2)
    Solution(solucion, start_time, 0)

def Part2():
    [lines, start_time] = Init(day, "2")
    solucion = 0
    bits = []
    lenth = len(CleanLine(lines[0]))
    for i in range(lenth):
        bits.append([0,0])
        
    for c in range(0, len(lines)):
        line = lines[c] = CleanLine(lines[c])

        for index, l in enumerate(line):
            if l == "0":
                bits[index][0] += 1
            else:
                bits[index][1] += 1
    
    aux = lines
    for index in range(lenth):
        subList = TakeTwoList(index, aux)
        if len(subList[0]) > len(subList[1]):
            aux = subList[0]
        else:
            aux = subList[1]
        if len(aux) <= 1:
            break
    oxygen = int(aux[0],2)
    print(f"\nOxygen generator rating: {aux} {oxygen}")

    aux = lines
    for index in range(lenth):
        subList = TakeTwoList(index, aux)
        if len(subList[0]) > len(subList[1]):
            aux = subList[1]
        else:
            aux = subList[0]
        if len(aux) <= 1:
            break
        
    co2 = int(aux[0],2)
    print(f"\nCO2 scrubber rating: {aux} {co2}")
    
    solucion = co2 * oxygen
    Solution(solucion, start_time, 0)

#Part1()
Part2()