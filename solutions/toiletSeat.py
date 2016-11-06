path = input()
initial = path[0]
path = path[1:]
sum = 0
if path[0] != initial:
    sum = sum + 1
if path[0] == "D":
    sum = sum + 1

for i in range(1,len(path)):
    if path[i] == "D":
        sum = sum + 2
print(sum)
# all down policy
sum = 0
if path[0] != initial:
    sum = sum + 1
if path[0] == "U":
    sum = sum + 1

for i in range(1,len(path)):
    if path[i] == "U":
        sum = sum + 2

print(sum)
#all u want
sum = 0
if path[0] != initial:
    sum = sum + 1

for i in range(len(path)-1):
    if path[i] != path[i+1]:
        sum += 1
print(sum)
