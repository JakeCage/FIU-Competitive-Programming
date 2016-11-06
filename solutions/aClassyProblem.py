
numTests = int(input())
for test in range(numTests):
    numPeople = int(input())
    classMap = {}
    classList = []
    nameList = []


    for line in range(numPeople):
        person = input()
        person = person.split()
        name = person[0][:-1]
        classiness = person[1].split('-')
        newclassiness = ""

        for c in reversed(classiness):
            if c == "upper":
                newclassiness += 'A'
            elif c == "middle":
                newclassiness += 'B'
            else:
                newclassiness += 'C'

        classList.append(newclassiness)
        nameList.append(name)

    maxLen = len(max(classList ,key=len))
    for i in range(len(classList)):
        while len(classList[i]) != maxLen:
            classList[i] += 'B'
        if classList[i] in classMap:
            classMap[classList[i]].append(nameList[i])
            classMap[classList[i]] = sorted(classMap[classList[i]])
        else:
            classMap[classList[i]] = [nameList[i]]

    for c in sorted(classList):
        print(classMap[c].pop(0))
    print("==============================")