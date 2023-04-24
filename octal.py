def octal():
    num = int(input("enter a number: "))
    octal = ''
    while(num > 0):
        octal = str(num % 8) + octal
        num //= 8
    print(octal)

#run function
octal()