def answer(maze):
    visited = set()
    queue = []
    mazeHeight = len(maze)
    mazeWidth = len(maze[0])
    queue.append(((0,0),1,0))
    visited.add(((0,0),0))
    while queue:
        yx,distance, cost = queue.pop(0)
        y,x = yx
        if yx == (mazeHeight-1,mazeWidth-1):
            return distance

        if cost == 0:
            if y+2 < mazeHeight:
                if not maze[y+2][x] and (y+2,x,cost+1) not in visited and maze[y+1][x] == 1:
                    queue.append(((y+2,x),distance+2, cost+1))
                    visited.add((y+2,x,cost+1))

            if y-2 >= 0:
                if not maze[y-2][x] and (y-2,x,cost+1) not in visited and maze[y-1][x] == 1:
                    queue.append(((y-2,x),distance+2, cost+1))
                    visited.add((y-2,x,cost+1))

            if x+2 < mazeWidth:
                if not maze[y][x+2] and (y,x+2,cost+1) not in visited and maze[y][x+1] == 1:
                    queue.append(((y,x+2),distance+2, cost+1))
                    visited.add((y,x+2,cost+1))

            if x-2 >= 0:
                if not maze[y][x-2] and (y,x-2,cost+1) not in visited and maze[y][x-1] == 1:
                    queue.append(((y,x-2),distance+2, cost+1))
                    visited.add((y,x-2,cost+1))

        if y+1 < mazeHeight:
            if not maze[y+1][x] and (y+1,x,cost) not in visited:
                queue.append(((y+1,x),distance+1, cost))
                visited.add((y+1,x,cost))

        if y-1 >= 0:
            if not maze[y-1][x] and (y-1,x,cost) not in visited:
                queue.append(((y-1,x),distance+1, cost))
                visited.add((y-1,x,cost))

        if x+1 < mazeWidth:
            if not maze[y][x+1] and (y,x+1,cost) not in visited:
                queue.append(((y,x+1),distance+1, cost))
                visited.add((y,x+1,cost))

        if x-1 >= 0:
            if not maze[y][x-1] and (y,x-1,cost) not in visited:
                queue.append(((y,x-1),distance+1, cost))
                visited.add((y,x-1,cost))

    return False

print(answer([
    [0,1,1,0,1],
    [0,0,0,0,0],
    [1,1,1,0,0],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,0,0]
]))