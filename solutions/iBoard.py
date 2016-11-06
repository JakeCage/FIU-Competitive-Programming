import sys

for st in sys.stdin:
    st = st.replace("\n", "")
    st = ' '.join(format(ord(x), 'b') for x in st)
    st = st.split(' ')

    for i in range(len(st)):
        while len(st[i]) != 7:
            st[i] = '0' + st[i]
        st[i] = st[i][::-1]

    st = ''.join(st)
    leftPressed = False
    rightPressed = False
    for c in st:
        if c == '1':
            leftPressed = not leftPressed
        else:
            rightPressed = not rightPressed

    if leftPressed or rightPressed:
        print("trapped")
    else:
        print("free")