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
