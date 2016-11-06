for i in range(int(input())):
    command = input()
    if command[0:10] == "Simon says":
        print(command[11:])