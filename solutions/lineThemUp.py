names = []
for i in range(int(input())):
    names.append(input())

answer = "NONE"

for i in range(len(names)-1):
    if names[i].lower() > names[i+1].lower():
        if answer == "NONE":
            answer = "DECREASING"
        elif answer == "INCREASING":
            answer = "NEITHER"
            break
        else:
            pass
    elif names[i].lower() < names[i+1].lower():
        if answer == "NONE":
            answer = "INCREASING"
        elif answer == "DECREASING":
            answer = "NEITHER"
            break
        else:
            pass

print(answer)