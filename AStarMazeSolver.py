from helper_main import *

def Sort(sub_li):
#fungsi sorting berdasarkan element sub list kedua
    sub_li.sort(key = lambda x: x[1])
    return sub_li

def MapDraw(mat,path) :
    for x in range(0,len(mat)):
        for y in range(0,len(mat[x])):
            if ([x,y] in path):
                assert mat[x][y] in ("x","3")
                print("-",end=" ")
            elif (mat[x][y]=='1'):
                print("+",end=" ")
            elif (mat[x][y]=='3'):
                print("*",end=" ")
            else:
                print(' ',end=" ")
        print()

def isSafe(y,x,mat) :
    if ((x>=0) and (y>=0) and (x<len(mat)) and (y<len(mat[0]))) :
        return True
    return False

def solveMazeAStar():
#symbol dan artinya
#1 = dinding, 0 = jalan, x = visited
    path=[]
    maze = inputMatrixFromFile()
    start = [1,0]#[1,0] #(baris,kolom) atau (y,x)
    path.append(start)
    end = [30,30]#[27,40]#[30,30]#[1,20]#[9,10]#
    maze[end[0]][end[1]] = "3"
    now = start
    maze[now[0]][now[1]] = "x"
    queue = []
    StepCount = 0 # g(n)
    while now != end:
        StepCount+=10
        #check kiri
        if isSafe(now[1]-1,now[0],maze):
            if (maze[now[0]][now[1]-1] == "0")or(maze[now[0]+1][now[1]] == "3"):
                coor = [now[0],now[1]-1] #koordinat kiri maze saat ini
                subqueue = []
                subqueue.append(coor)
                StepPredict = abs(now[0]-end[0])+abs(now[1]-1-end[1])#fungsi h(n) heuristik jarak y+x
                subqueue.append(StepCount+StepPredict) #f(n)
                queue.append(subqueue)
        #check atas
        if isSafe(now[1],now[0]-1,maze):
            if (maze[now[0]-1][now[1]] == "0")or(maze[now[0]-1][now[1]] == "3"):
                #print("masuk")
                coor = [now[0]-1,now[1]] #koordinat atas maze saat ini
                subqueue = []
                subqueue.append(coor)
                StepPredict = abs(now[0]-1-end[0])+abs(now[1]-end[1])#fungsi h(n) heuristik jarak y+x
                subqueue.append(StepCount+StepPredict) #f(n)
                queue.append(subqueue)
        #check kanan
        if isSafe(now[1]+1,now[0],maze):
            if (maze[now[0]][now[1]+1] == "0")or(maze[now[0]][now[1]+1] == "3"):
                coor = [now[0],now[1]+1] #koordinat kanan maze saat ini
                subqueue = []
                subqueue.append(coor)
                StepPredict = abs(now[0]-end[0])+abs(now[1]+1-end[1])#fungsi h(n) heuristik jarak y+x
                subqueue.append(StepCount+StepPredict) #f(n)
                queue.append(subqueue)
        #check bawah
        if isSafe(now[1],now[0]+1,maze):
            if (maze[now[0]+1][now[1]] == "0")or(maze[now[0]+1][now[1]] == "3"):
                coor = [now[0]+1,now[1]] #koordinat bawah maze saat ini
                subqueue = []
                subqueue.append(coor)
                StepPredict = abs(now[0]+1-end[0])+abs(now[1]-end[1])#fungsi h(n) heuristik jarak y+x
                subqueue.append(StepCount+StepPredict) #f(n)
                queue.append(subqueue)
        ########
        queue = Sort(queue)
        now = queue[0][0]
        del queue[0]
        maze[now[0]][now[1]] = "x"
        path.append(now)
    pathFix = pathMaker(path)
    solve = [maze,pathFix]
    return solve

def checkPoint(pathElmt,now) :
    if ((now[0] == pathElmt[0]) and ((now[1] <= pathElmt[1]+1) and (now[1] >= pathElmt[1] - 1))) :
        return True
    if ((now[1] == pathElmt[1]) and ((now[0] <= pathElmt[0]+1) and (now[0] >= pathElmt[0] - 1))) :
        return True
    else :
        return False

def pathMaker(path) :
    i = len(path)-1
    while i > 0 :
        if checkPoint(path[i],path[i-1]) == False :
            del path[i-1]
        i -= 1
    return path

def main():
    solve = solveMazeAStar()
    MapDraw(solve[0],solve[1])

main()
