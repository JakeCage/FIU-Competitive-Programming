line = input()
password,string = line.split()
string = list(string)
passed = True

try:
    for i in range(len(password)-1):
        firstidx = string.index(password[i])
        sndidx = string.index(password[i+1])
        if firstidx > sndidx:
            print("FAIL")
            passed = False
            break
        string.pop(firstidx)
    if passed:
        print("PASS")

except:
    print("FAIL")