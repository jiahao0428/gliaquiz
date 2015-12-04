def combanation(x,y):
    if y == 1:
        return x
    elif x == y:
        return 1
    return combanation(x-1, y) + combanation(x-1, y-1)

print combanation(40, 10)
print combanation(990, 33)
