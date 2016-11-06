#Go through a sorted list and print the integers 0-99 that are missing from it

def miss(arr):
    i = 0
    print(arr)
    while i < len(arr)-1:
        if arr[i+1] - arr[i] == 2:
            print(arr[i]+1)
        elif arr[i+1] - arr[i] > 2:
            print(str(arr[i]+1) + "-" + str(arr[i+1]-1))
        i += 1

miss(sorted([88, 105, 3, 2, 200, 0, 10]))