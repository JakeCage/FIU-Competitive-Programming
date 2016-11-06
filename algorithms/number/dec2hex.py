converter = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

def dec2num(num):
    global converter

    if num == 0:
        pass
    elif num == 1:
        print(1,end='')
    else:
        dec2num(num//16)
        x = num%16
        if x <= 9:
            print(x, end='')
        else:
            print(converter[x],end='')


dec2num(5)