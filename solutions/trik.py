ball = 1
for char in input():
    if char == 'A':
        if ball == 1:
            ball = 2
        elif ball == 2:
            ball = 1

    elif char == 'B':
        if ball == 2:
            ball = 3
        elif ball == 3:
            ball = 2

    else:
        if ball == 1:
            ball = 3
        elif ball == 3:
            ball = 1

print(ball)