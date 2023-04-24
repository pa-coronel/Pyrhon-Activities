def prime():
    num = int(input("enter a number: "))
    count = 0
    for i in range(num):
        if num % (i + 1) == 0:
            count += 1
    if count > 2:
        print("not prime")
    else:
        print("is prime")

#run function
prime()