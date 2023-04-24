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

#run function
xo()