from random import randint


MAP = [[2,1,0,0,0,0],[0,1,0,0,0,0],[0,1,0,0,0,0],[0,0,0,0,1,0],[0,0,0,0,1,0]]
POS = [0,0]
TB = 0

def spawnTarget(map,tb):
    global MAP
    global TB
    if tb == 0:
        while 1:
            x = randint(0,5)
            y = randint(0,5)
            if(MAP[y][x] == 0):
                MAP[y][x] = 3
                TB == 1
                break

def printMap(map):
    for y in map:
        s = ""
        for x in y:
            if(x == 0):
                s += "O"
            if(x == 1):
                s += "W"
            if(x == 2 ):
                s += "h"
            if(x == 3):
                s += "X"
            s += " "
        print(s,"\n")
    print("======================")

def game(map):
    opr = input()
    global MAP
    global POS
    global TB
    if(opr == "8"):
        if(POS[1] > 0 and MAP[POS[1]-1][POS[0]] == 0):
            MAP[POS[1]][POS[0]] = 0
            POS[1] -= 1 
            MAP[POS[1]][POS[0]] = 2
            return 0
    if(opr == "2"):
        if(POS[1] < len(MAP)-1 and MAP[POS[1]+1][POS[0]] == 0):
            MAP[POS[1]][POS[0]] = 0
            POS[1] += 1
            MAP[POS[1]][POS[0]] = 2
            TB = 1
            return 0
    if(opr == "4"):
        if(POS[0] > 0 and MAP[POS[1]][POS[0]-1] == 0):
            MAP[POS[1]][POS[0]] = 0
            POS[0] -= 1
            MAP[POS[1]][POS[0]] = 2
            return 0
    if(opr == "6"):
        if(POS[0] < len(MAP[0])-1 and MAP[POS[1]][POS[0]+1] == 0):
            MAP[POS[1]][POS[0]] = 0
            POS[0] += 1
            MAP[POS[1]][POS[0]] = 2
            return 0
    if(len(opr) == 2 and opr[0] == "5"):
        if(opr[1] == "8"):
            for i in range(0,POS[1]):
                if(MAP[i][POS[0]] == 3):
                    MAP[i][POS[0]] = 0
                    TB = 0
        if(opr[1] == "2"):
            for i in range(POS[1],len(MAP)-1):
                if(MAP[i][POS[0]] == 3):
                    MAP[i][POS[0]] = 0
                    TB = 0
        if(opr[1] == "4"):
            for i in range(0,POS[0]):
                if(MAP[i][POS[0]] == 3):
                    MAP[POS[1]][i] = 0
                    TB = 0
        if(opr[1] == "6"):
            for i in range(POS[0],len(MAP[0])-1):
                if(MAP[i][POS[0]] == 3):
                    MAP[POS[1]][i] = 0
                    TB = 0

while 1:
    printMap(MAP)
    game(MAP)
    spawnTarget(MAP,TB)
    
