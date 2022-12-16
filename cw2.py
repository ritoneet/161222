# # classic
# def f(a, b):
#     c = b
#     b = a
#     a = c
#     return a, b
#
#
# # python
# def f1(a, b):
#     a, b = b, a
#     return a, b
#
#
# # all
# def f2(a, b):
#     return b, a
#
#
# a = 1
# b = 5
# print(f(a, b))
# b, a = f(a, b)
# print(f"a = {a}, b = {b}")
#
# a = 1
# b = 5
# print(f1(a, b))
# b, a = f1(a, b)
# print(f"a = {a}, b = {b}")
#
# a = 1
# b = 5
# print(f2(a, b))
# b, a = f2(a, b)
# print(f"a = {a}, b = {b}")

c = 30
a = 30
b = 30
a, b, c = c, c, c
print(a)
print(b)
print(c)
