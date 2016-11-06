#arr = list(map(int, input().split()))
result = 0
for iter in range(int(input())):
    num = input()
    result += pow(int(num[:-1]),int(num[-1]))
print(result)