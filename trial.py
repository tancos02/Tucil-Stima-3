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

def BFS(x,y,mat): 
    queue = deque( [(x,y,None)]) #create queue 
    while len(queue)>0: #make sure there are nodes to check left 
        node = queue.popleft() #grab the first node 
        x = node[0] #get x and y 
        y = node[1] 
        if mat[x][y] == "3": #check if it's an exit 
            return PathMaker(node) #if it is then return the path 
        if (mat[x][y]!="0"): #if it's not a path, we can't try this spot 
            continue 
        mat[x][y]="2" #make this spot explored so we don't try again 
        for i in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]: #new spots to try 
            queue.append((i[0],i[1],node))#create the new spot, with node as the parent 
    return [] 

def MapDrawBFS(mat,path) :
    for x in range(0,len(mat)): 
        for y in range(0,len(mat[x])): 
            if ((x,y) in path): 
                assert mat[x][y] in ("2","3") 
                print("-",end=" ") 
            elif (mat[x][y]=='1'): 
                print("+",end=" ") 
            elif (mat[x][y]=='3'): 
                print("*",end=" ") 
            else: 
                print(' ',end=" ") 
        print() 

def main() :
    fileName = "input.txt"
    mat = matrixReader(fileName)
    print("Input Maze : ")
    MapDrawBFS(mat,[])
    print("Starting Point : ")
    start = np.zeros((2,),dtype = int)
    start[0] = int(input())
    start[1] = int(input())
    print("Finish Point : ")
    finish = np.zeros((2,),dtype = int)
    finish[0] = int(input())
    finish[1] = int(input())
    mat[finish[0]][finish[1]] = '3'
    MapDrawBFS(mat,BFS(start[0],start[1],mat))

main()
