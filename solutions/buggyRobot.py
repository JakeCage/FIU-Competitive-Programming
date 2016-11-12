def readCommand(icyx, commands):
    global height
    global width

    i,cost,y,x = icyx
    if commands[i] == 'L' and isValid(y,x-1,height,width):
        x -= 1
    elif commands[i] == 'R' and isValid(y, x+1,height,width):
        x += 1
    elif commands[i] == 'U' and isValid(y-1,x, height,width):
        y -= 1
    elif commands[i] == 'D' and isValid(y+1,x,height,width):
        y += 1

    i += 1
    return (i,cost,y,x)
def deleteCommand(icyx):
    i, cost, y, x = icyx

    return (i+1, cost+1, y,x)
def addCommands(icyx):
    global height
    global width

    i,cost,y,x = icyx
    acceptableAdd = []

    cost += 1

    if isValid(y,x-1,height,width):
        acceptableAdd.append((i,cost,y,x-1))
    if isValid(y, x+1,height,width):
        acceptableAdd.append((i,cost,y,x+1))
    if isValid(y-1,x, height,width):
        acceptableAdd.append((i,cost,y-1,x))
    if isValid(y+1,x,height,width):
        acceptableAdd.append((i,cost,y+1,x))

    return acceptableAdd

def isValid(y,x,height,width):
    if y >= 0 and y < height and x >= 0 and x < width:
        if grid[y][x] != '#':
            return True

    return False

hw = input()
hw = hw.split()
height, width = [int(num) for num in hw]

grid = []

for i in range(height):
    grid.append(list(input()))

startFound = False
endFound = False

for y in range(height):
    for x in range(width):
        if grid[y][x] == 'R':
            startFound = True
            queue =[(0,0,y,x)]
            visited = set([(0,0,y,x)])
        if grid[y][x] == 'E':
            exit = (y,x)
            endFound = True
        if startFound and endFound:
            break

minChanges = -1
commands = input()
commandCount = len(commands)

while queue:
    icyx = queue.pop(0)

    if icyx[1] < minChanges or minChanges == -1:
        curr = readCommand(icyx, commands)

        if (curr[2],curr[3]) == exit:
            if minChanges == -1 or curr[1] < minChanges:
                minChanges = curr[1]
        elif curr[0] < commandCount:
            if curr not in visited:
                queue.append(curr)
                visited.add(curr)
        curr = deleteCommand(icyx)
        if curr[0] < commandCount and (minChanges == -1 or curr[1] < minChanges) and curr not in visited:#xor
            queue.append(curr)
            visited.add(curr)

        for add in addCommands(icyx):
            if (add[2],add[3]) == exit:
                if minChanges == -1 or add[1] < minChanges:
                    minChanges = add[1]
            else:
                if add not in visited:
                    queue.append(add)
                    visited.add(curr)

print(minChanges)