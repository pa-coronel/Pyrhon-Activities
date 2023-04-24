# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def parenthesis():
    word = input("enter a word: ").lower()
    encoded = ""

    for i in word:
        count = 0
        for j in word:
            if i == j:
                count += 1
        if count > 1:
            encoded += ')'
        else:
            encoded += '('

    print("the word:", encoded,)

def camelcase():
    word = input("enter a word: ")
    newword = ''
    for i in word:
        if i.isupper():
            newword += " "
        newword += i

    print("the word:", newword)

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

def findUniq():
    num = [2, 2, 2, 1, 2, 2, 2]
    num = sorted(num)
    uniq = 0

    if num[0] != num[1]:
        uniq = num[0]
    else:
        uniq = num[len(num) - 1]

    print(uniq)

def weirdStringCase():
    asked = input("enter a word: ") + ' '

    words = ''
    temp = ''

    for i in asked:
        if i == ' ':
            if len(temp) % 2 == 0:
                words += temp.upper() + ' '
            else:
                words += temp.lower() + ' '
            temp = ''
        else:
            temp += i

    print(words)

def xo():
    word = input("enter a word: ").lower()
    x = o = 0
    result = False

    for i in word:
        if i == 'x':
            x += 1
        elif i == 'o':
            o += 1

    if x == o:
        result = True

    print("result:", result)

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

def binary():
    num = int(input("enter a number: "))
    count = 1
    ra = []
    binary = ''
    while count <= num:
        ra.append(count)
        count *= 2
    ra.reverse()
    print(ra)
    for i in ra:
        if num >= i:
            binary += '1'
            num -= i
        else:
            binary += '0'
    print(binary)

def binary2():
    num = int(input("enter a number: "))
    binary = ''
    while(num > 0):
        binary = str(num % 2) + binary
        num //= 2
    print(binary)

def octal():
    num = int(input("enter a number: "))
    octal = ''
    while(num > 0):
        octal = str(num % 8) + octal
        num //= 8
    print(octal)

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

# run function

divide()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
