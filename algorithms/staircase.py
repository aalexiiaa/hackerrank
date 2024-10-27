def staircase(n):
    message = ""

    for i in range(n):
        message += ((n - i - 1) * ' ') + ((1 + i) * '#')

        if i != (n - 1):
            message += "\n"
 
    print(message)


staircase(6)   