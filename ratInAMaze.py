def printMaze(sol): # print the sol
    for i in sol:
        for j in i:
            print(j,end=" ")
        print()
def is_safe(maze,x,y): # check if the following block is 1 or 0 return False if it in 0
    N = len(maze)
    if x>=0 and y>=0 and y<N and x<N and maze[x][y] == 1:
        return True
    return False
def solveMazeUtil(maze,x,y,sol):   # backtracking algorithm
    if x == len(maze)-1 and y == len(maze)-1 and maze[x][y] == 1: # base case when we reach the target
        sol[x][y] = 1
        return True
    if is_safe(maze,x,y): # check if it is valid and put sol[x][y] = 1
        sol[x][y] = 1
        if solveMazeUtil(maze,x+1,y,sol): # pass the next horizontal cell
            return True
        if solveMazeUtil(maze,x,y+1,sol): # pass the next vertical cell to see the validation
            return True
        sol[x][y] = 0  # if both cases are false then put sol[x][y] = 0
        return False  # return False
def solveMaze(maze):
    N = len(maze)
    sol = [ [ 0 for j in range(N) ] for i in range(N) ] # creating a N*N matrix all value = 0
    if solveMazeUtil(maze,0,0,sol) == False:
        print("path does not exist")
    else:
        printMaze(sol)


maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]

solveMaze(maze)

