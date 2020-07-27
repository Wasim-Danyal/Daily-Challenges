def sevennotfive(x,y):
    lst = []
    for num in range(x,y):
        if num % 7 == 0 and num % 5 != 0:
            lst.append(num)
    return lst











print(sevennotfive(2000,3200))