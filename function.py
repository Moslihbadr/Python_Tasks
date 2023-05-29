def test(*args):
    print(args)

args = [2, 4, 6]
print(type(args))

test(*args)
