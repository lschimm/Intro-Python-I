"""Tuesday's Lecture!"""

"""Tuples are lists that are immutable"""
# i.e. ...
a = (1, 2, 3)
a[0] = 20  # CAN'T DO

a[0]

# Passing by value - interger or string


def foo(x):
    x = 10


a = 20

foo(a)

print(a)

# Passing by reference - tuple, lists, dictionaries, objects etc


def bar(x):
    x.append(99)


a = [1, 2, 3]

bar(a)

print(a)
