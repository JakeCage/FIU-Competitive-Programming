import itertools

for iter in range(int(input())):
    hashmap = {}
    passed = False
    line = input()
    line = [int(elem) for elem in line.split()]
    count = line.pop(0)
    for L in range(1, count+1):
      for subset in list(itertools.combinations(line, L)):
        var = True
        if sum(subset) in hashmap:
            for element in hashmap[sum(subset)]:
                if element in subset:
                    var = False
                    hashmap[sum(subset)] = subset
                    break
            if var:
                print("Case #" + str((iter+1)) + ":")
                for num in hashmap[sum(subset)]:
                    print(num, end=" ")
                print()
                for num in subset:
                    print(num, end=" ")
                passed = True
                break
        else:
            hashmap[sum(subset)] = subset
      if passed:
            break
    if not passed:
        print("Case #" + str((iter+1)) + ":")
        print("Impossible")

    print()