a = 48679243
b = 0
print("a ", a)
while a > 0:
    c = a % 10
    b = (b * 10) + c
    a = a // 10
print("b ", b)