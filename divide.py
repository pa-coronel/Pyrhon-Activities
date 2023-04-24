def divide():
    num1 = int(input("enter a number[1]: "))
    num2 = int(input("enter a number[2]: "))
    count = 0
    temp = 0

    while (num1 > temp):
        temp += num2
        if (num1 < temp):
           break
        count += 1
    print("quotient:", count)

#run function
divide()