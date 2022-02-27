# n進数から10進数に変換
print (int('100', 2))

# 10進数からn進数に変換
def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)
