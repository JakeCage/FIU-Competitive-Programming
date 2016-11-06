for iter in range(int(input())):
    arr = list(map(int, input().split()))
    curr = 1
    result = 0
    for i in range(1,len(arr)):
        pack = curr*2
        if pack < arr[i]:
            result += (arr[i] - pack)
        curr = arr[i]
    print(result)