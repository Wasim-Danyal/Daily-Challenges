def name(str):
    count = 0
    bob = str.split()
    for i in bob:
        if i == "am":
            count += 1
    return count

