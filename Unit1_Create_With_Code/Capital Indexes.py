
def capital_indexes(s):
    lst = []
    for index, ch in enumerate(s):
        if ch.isupper():
            lst.append(index)
    return lst
print (capital_indexes("Hel l A"))