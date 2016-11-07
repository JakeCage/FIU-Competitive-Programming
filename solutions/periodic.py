string = input()

minlen = len(set(string))
endi = minlen

currstring = string[0:endi]

starti = endi
endi = endi+len(currstring)

if minlen == 1:
    print(1)
else:
    while len(string) % len(currstring) != 0:
        minlen += 1
        currstring = string[0:minlen]
        starti = minlen
        endi = minlen+len(currstring)

    while True:
        if len(string) == len(currstring):
            print(minlen)
            break
        if len(string) % len(currstring) == 0:
            if currstring[-1]+currstring[0:-1] == string[starti:endi]:
                currstring = string[starti:endi]
                start = endi
                endi = endi+len(currstring)

                if endi > len(string):
                    print(minlen)
                    break
            else:
                minlen += 1
                currstring = string[0:minlen]
                starti = minlen
                endi = minlen+len(currstring)
        else:
            minlen += 1
            currstring = string[0:minlen]
            starti = minlen
            endi = minlen+len(currstring)
