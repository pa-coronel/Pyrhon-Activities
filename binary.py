def binary():
    num = int(input("enter a number: "))
    binary = ''
    while(num > 0):
        binary = str(num % 2) + binary
        num //= 2
    print(binary)

#run function
binary()