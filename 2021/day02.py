from libs.functions import *

day = 2


def Part1():
    [lines, start_time] = Init(day, "1")
    solucion = 0
    position = [0,0]
    for c in range(0, len(lines)):
        line = CleanLine(lines[c])
        instruction = line.split(" ")
        if instruction[0] == "forward":
            position[0] += int(instruction[1])
        elif instruction[0] == "down":
            position[1] += int(instruction[1])
        elif instruction[0] == "up":
            position[1] -= int(instruction[1])
        print(line,position)
    
    solucion = position[0] * position[1]

    Solution(solucion, start_time, 0)

def Part2():
    [lines, start_time] = Init(day, "2")
    solucion = 0
    position = [0,0,0]
    for c in range(0, len(lines)):
        line = CleanLine(lines[c])
        instruction = line.split(" ")
        if instruction[0] == "forward":
            position[1] += int(instruction[1])*position[2]
            position[0] += int(instruction[1])
        elif instruction[0] == "down":
            position[2] += int(instruction[1])
        elif instruction[0] == "up":
            position[2] -= int(instruction[1])
        print(line,position)
    
    solucion = position[0] * position[1]

    Solution(solucion, start_time, 0)

Part1()
Part2()