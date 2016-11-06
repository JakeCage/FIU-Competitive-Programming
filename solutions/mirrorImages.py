for i in range(int(input())):
    xylen = input()

    xylen = xylen.split()
    grid = []
    for iter in range(int(xylen[0])):
        grid.append(list(input()))
    print("Test " + str(i+1))
    for g in reversed(grid):
        print(''.join(reversed(g)))