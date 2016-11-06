while True:
    cases = int(input())
    if cases == -1:
        break

    prev = 0
    miles = 0
    for i in range(cases):
        mph,curr = map(int, input().split(' '))
        miles += mph*(curr-prev)
        prev = curr

    print(str(miles) + " miles")