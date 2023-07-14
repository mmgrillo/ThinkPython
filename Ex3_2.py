


def do_twice(f, value):
    f(value)
    f(value)

def print_twice(a):
    print(a)
    print(a)

print(do_twice(print_twice, "spam"))


