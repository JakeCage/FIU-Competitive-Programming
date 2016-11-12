hr = input()

houseCount, range = hr.split()

houseCount = int(houseCount)
range = int(range)
positions = input()
positions = positions.split()
positions = [int(num) for num in positions]
positions = sorted(positions)
i = 0
sum = 0

while positions:
    sum += 1
    i = positions[0]+range+range
    while i-range not in positions:
        i -= 1
    while positions:
        if positions[0] <= i:
            positions.pop(0)
        else:
            break

print(sum)