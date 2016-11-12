import bisect

tmp = input()
tmp = tmp.split()
tmp = [int(x) for x in tmp]

total,countRanges = tmp
ranges = []
rangeSums = []

def sumRange(range):
    return range[1]-(range[0]-1)

for i in range(countRanges):
    r1 = input()
    r1 = r1.split()
    r1 = [int(num) for num in r1]
    ranges.append(r1)

ranges = sorted(ranges)
starts = []
ends = []


for r1 in ranges:
    starts.append(r1[0])
    ends.append(r1[1])
    rangeSums.append(sumRange(r1))

maximum = 0

for i in range(countRanges):
    checki = bisect.bisect(starts[i:],ends[i])
    if ends[i] < starts[checki]:
        next = rangeSums[i]+max(rangeSums[checki:])
        if next > maximum:
            maximum = next

print(total-maximum)