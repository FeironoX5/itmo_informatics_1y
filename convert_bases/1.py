import math


def to_custom_base(x, b, prec=30):
    print(x, b, prec)
    k = math.floor(math.log(x, b)) + 1
    # Минимальная степень, в которую нужно
    # возвести b, чтобы получилось число больше x
    res = ""
    for i in range(k - 1, -prec - 1, -1):
        if len(res) == k:
            res += "."
        digit = math.floor((x / (b ** i)) % b)
        x -= digit * (b ** i)
        res += str(digit)
        i -= 1
    return res


print(to_custom_base(float(input()), int(input())))
