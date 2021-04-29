def a(*args):
    y=len(args)
    total = sum(args)

    if y == 0:
        return 0
    else:
        return total/y

print(a(5,8))

