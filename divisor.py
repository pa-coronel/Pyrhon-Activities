def divisor():
    num = int(input("enter a number: "))
    ra = []

    for i in range(num):
        if num % (i + 1) == 0:
            if i + 1 != 1:
                ra.append(i + 1)
    if len(ra) == 1:
        print("the integer is prime")
    else:
        for i in ra:
            print(i)

#run function
divisor()