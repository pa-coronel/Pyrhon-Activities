def tower():
    height = int(input("enter tower height: "))
    count = 1
    ra = []
    for i in range(height):
        k = height - i - 1
        temp = ''
        while k > 0:
            k -= 1
            temp += " "
        for j in range(count):
            temp += "*"
        count += 2
        ra.append(temp)

    for i in ra:
        print(i)

#run function
tower()