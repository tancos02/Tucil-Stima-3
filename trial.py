# trial.py
import numpy as np
from collections import deque 

def matrixReader (fileName) :
    l = np.loadtxt(fileName,dtype = str)
    return (l)

def PathMaker(node) :
    path = []
    while(node != None) :
        path.append((node[0],node[1])) 
        node = node[2] 
    return(path)

def BFS(mat,x,y) :
    queue = deque([(x,y,None)])
    while (len(queue) > 0) :
        node = queue.popleft()
        x = node[0]
        y = node[1]
        if(mat[x][y] == '3') :
            return (PathMaker(node))
        if(mat[x][y] != '0') :
            continue
        mat[x][y] == '2'
        for i in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]] :
            queue.append((i[0],i[1],node))
    return []

def MapDrawBFS(mat,path) :
    for x in range(0,len(mat)): 
        for y in range(0,len(mat[x])): 
            if ((x,y) in path): 
                assert mat[x][y] in ('0','3') 
                print("-",end="") 
            elif (mat[x][y]=='1'): 
                print("+",end="") 
            elif (mat[x][y]=='3'): 
                print("*",end="") 
            else: 
                print(' ',end="") 
        print() 

def main() :
    fileName = "input.txt"
    mat = matrixReader(fileName)
    print("Input Maze : ")
    print(mat)
    print("Starting Point : ")
    start = np.zeros((2,),dtype = int)
    start[0] = int(input())
    start[1] = int(input())
    print("Finish Point : ")
    finish = np.zeros((2,),dtype = int)
    finish[0] = int(input())
    finish[1] = int(input())
    mat[finish[0]][finish[1]] = "3"
    print(mat)
    MapDrawBFS(mat,BFS(mat,start[0],start[1]))

main()