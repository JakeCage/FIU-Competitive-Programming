min = int(input())
max = int(input())+1

requiredSum = int(input())
for i in range(min, max):
    if sum(map(int, list(str(i)))) == requiredSum:
        print(i)
        break

for i in reversed(range(min, max)):
    if sum(map(int, list(str(i)))) == requiredSum:
        print(i)
        break