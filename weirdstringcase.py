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

#run function
weirdStringCase()