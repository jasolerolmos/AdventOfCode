from classes import Solution, Init

def Part1():
    [lines, start_time] = Init(1, 1)
    Solution(lines[0].count('(') - lines[0].count(')'), start_time, 0)

def Part2():
    [lines, start_time] = Init(1, 2)
    solucion = 0
    for index in enumerate(lines[0]):
        if index[1] == '(':
            solucion += 1
        else:
            solucion -= 1
        if solucion == -1:
            solucion = index[0]+1
            break
    
    Solution(solucion, start_time, 0)


Part1()
Part2()
