def findUniq():
    num = [2, 2, 2, 1, 2, 2, 2]
    num = sorted(num)
    uniq = 0

    if num[0] != num[1]:
        uniq = num[0]
    else:
        uniq = num[len(num) - 1]

    print(uniq)

#run function
findUniq()