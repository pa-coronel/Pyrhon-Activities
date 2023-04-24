def camelCase():
    word = input("enter a word: ")
    newword = ''
    for i in word:
        if i.isupper():
            newword += " "
        newword += i

    print("the word:", newword)
    
#run function
camelCase()
