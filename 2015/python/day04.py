from classes import Solution, Init, CleanLine
import math
import hashlib

day = 4

def Part1():
    [lines, start_time] = Init(day, "1")
    solucion = lines[0]

    print(f"{hashlib.md5((solucion).encode('utf-8')).hexdigest()}")

    for c in range(0, int(math.pow(10,10))):
        code = hashlib.md5((solucion+str(c)).encode('utf-8')).hexdigest()
        
        if code.startswith("00000"):
            print(f"{code} => {str(c)}")
            solucion = str(c)
            break
    
    Solution(solucion, start_time, 0)


def Part2():
    [lines, start_time] = Init(day, "1")

    Solution(0, start_time, 0)
  


Part1()