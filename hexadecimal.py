def hexadecimal():
    num = int(input("enter a number: "))
    letters = "ABCDEF"
    hexadec = ""
    while (num > 0):
        if(num % 16 > 9):
            hexadec = letters[(num % 16) % 10] + hexadec
        else:
            hexadec = str(num % 16) + hexadec
        num //= 16
    print(hexadec)

#run function
hexadecimal()