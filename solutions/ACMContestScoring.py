problems = {}
while True:
    line = input()
    if line == "-1":
        break

    line = line.split(' ')
    if line[1] not in problems:
        if line[2] == "wrong":
            problems[line[1]] = [20,0]
        else:
            problems[line[1]] = [int(line[0]),1]
    else:
        if line[2] == "wrong":
            problems[line[1]][0] += 20
        else:
            problems[line[1]][1] = 1
            problems[line[1]][0] += int(line[0])
time = 0
solved = 0
for key in problems:
    solved += problems[key][1]
    time += problems[key][0]*problems[key][1]

print(solved, time)