def expandedForm():
    num = input("enter a number: ")
    count = 1
    result = ''
    while count < int(num):
        count *= 10
    for i in num:
        count //= 10
        result += str(count * int(i))
        if count > 1:
            result += str(' + ')
    print(result)

#run function
expandedForm()