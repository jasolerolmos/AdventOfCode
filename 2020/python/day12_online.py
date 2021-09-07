with open ('day12Input.txt') as inp:
    EW = 0
    NS = 0
    dir = 90

    for line in inp:
        action = line[0]
        num = int(line[1:])
        if action == "F" and dir == 90 or action == "E":
            EW += num
        elif action == "F" and dir == 180 or action == "S":
            NS -= num
        elif action == "F" and dir == 270 or action == "W":
            EW -= num
        elif action == "F" and dir == 0 or action == "N":
            NS += num
        elif action == "L":
            dir -= num
            if dir == 360 or dir == -360:
                dir = 0
            if dir == -90:
                dir = 270
            if dir == -180 or dir == 540:
                dir = 180
            if dir == -270 or dir == 450:
                dir = 90

        elif action == "R":
            dir += num
            if dir == 360 or dir == -360:
                dir = 0
            if dir == -90:
                dir = 270
            if dir == -180 or dir == 540:
                dir = 180
            if dir == -270 or dir == 450:
                dir = 90

print(f"Manhatten Distance: {abs(NS)+ abs(EW)}")