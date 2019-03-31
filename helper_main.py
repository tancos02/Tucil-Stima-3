def inputMatrixFromFile():
    maze=[]
    with open("in.txt", "r") as fin:
        for line in fin:
            line = line.strip()
            mazeRow = [x for x in line]
            maze.append(mazeRow)
    #print(len(maze[1]))
    return maze
