from helper_main import *

def Sort(sub_li):
#fungsi sorting berdasarkan element sub list kedua
    sub_li.sort(key = lambda x: x[1])
    return sub_li

def printMaze(mazeP):
    for l in mazeP:
        print(l)

def solveMazeAStar():
#symbol dan artinya
#1 = dinding, 0 = jalan, 2 = visited, x = path
    maze = inputMatrixFromFile()
    printMaze(maze)
    start = [1,0] #(baris,kolom) atau (y,x)
    end = [9,10]
    now = start
    maze[now[0]][now[1]] = "x"
    queue = []
    StepCount = 0 # g(n)
    while now != end:
        StepCount+=1
        #check kiri
        if (now[1]-1>=0):
            if (maze[now[0]][now[1]-1] == "0"):
                coor = [now[0],now[1]-1] #koordinat kiri maze saat ini
                subqueue = []
                subqueue.append(coor)
                StepPredict = abs(now[0]-end[0])+abs(now[1]-end[1])#fungsi h(n) heuristik jarak y+x
                subqueue.append(StepCount+StepPredict) #f(n)
                queue.append(subqueue)
        #check atas
        if (now[0]-1>=0):
            if (maze[now[0]-1][now[1]] == "0"):
                coor = [now[0]-1,now[1]] #koordinat atas maze saat ini
                subqueue = []
                subqueue.append(coor)
                StepPredict = abs(now[0]-end[0])+abs(now[1]-end[1])#fungsi h(n) heuristik jarak y+x
                subqueue.append(StepCount+StepPredict) #f(n)
                queue.append(subqueue)
        #check kanan
        if (now[1]+1<=len(maze[0])-1):
            if (maze[now[0]][now[1]+1] == "0"):
                coor = [now[0],now[1]+1] #koordinat kanan maze saat ini
                subqueue = []
                subqueue.append(coor)
                StepPredict = abs(now[0]-end[0])+abs(now[1]-end[1])#fungsi h(n) heuristik jarak y+x
                subqueue.append(StepCount+StepPredict) #f(n)
                queue.append(subqueue)
        #check bawah
        if (now[0]+1<=len(maze)-1):
            if (maze[now[0]+1][now[1]] == "0"):
                coor = [now[0]+1,now[1]] #koordinat bawah maze saat ini
                subqueue = []
                subqueue.append(coor)
                StepPredict = abs(now[0]-end[0])+abs(now[1]-end[1])#fungsi h(n) heuristik jarak y+x
                subqueue.append(StepCount+StepPredict) #f(n)
                queue.append(subqueue)
        #check
        queue = Sort(queue)
        #print(now)
        #print(queue)
        #printMaze(maze)
        now = queue[0][0]
        del queue[0]
        maze[now[0]][now[1]] = "x"
    return maze

printMaze(solveMazeAStar())
