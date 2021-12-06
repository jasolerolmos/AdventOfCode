from libs.functions import *

day = 1


def Part1():
    [lines, start_time] = Init(day, "1")
    solucion = 0
    
    for c in range(0, len(lines)):
        if c > 0 :
            prev = cadena
            cadena = int(CleanLine(lines[c]))
            if prev < cadena:
                solucion += 1
                print(c,":",cadena,"(increased)")
            elif prev > cadena:
                print(c,":",cadena,"(decreased)")
            else:
                print(c,":",cadena,"(No Changes)")
        else:
            cadena = int(CleanLine(lines[c]))

            print(c,":",cadena,"(N/A - no previous measurement)")

    
    Solution(solucion, start_time, 0)

def Part2():
    [lines, start_time] = Init(day, "2")
    solucion = 0
    cadena = 9999999999999
    for c in range(0, len(lines)-2):
        prev = cadena
        cadena = int(CleanLine(lines[c])) + int(CleanLine(lines[c+1])) + int(CleanLine(lines[c+2]))
        print(CleanLine(lines[c]),CleanLine(lines[c+1]),CleanLine(lines[c+2]))
        if prev < cadena:
            solucion += 1
            print(c,":",cadena,"(increased)")
        elif prev > cadena:
            print(c,":",cadena,"(decreased)")
        else:
            print(c,":",cadena,"(No Changes)")

    
    Solution(solucion, start_time, 0)

Part1()
Part2()