import math

digits = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}


def from_custom_base(x, b):
    res = 0
    i = x.index('.') - 1 if '.' in x else len(x) - 1
    for c in list(x):
        if c != '.':
            d = digits[c]
            res += d * (b ** i)
            i -= 1
    return res


def to_custom_base(x, b, prec=8):  # вопрос?? можно ирр. x?
    # Получим b-разложение x
    k = math.floor(math.log(x, b)) + 1
    res = ""
    for i in range(k - 1, -prec - 1, -1):
        digit = math.floor((x / (b ** i)) % b)
        x -= digit * (b ** i)
        res += ('.' + str(digit) if len(res) == k else str(digit))
    return res


def convert(x, from_base, to_base):
    return to_custom_base(from_custom_base(x, from_base), to_base)


if __name__ == '__main__':
    x = input('Число: ')
    from_base = int(input('Из СИ: '))
    to_base = int(input('В СИ: '))
    print(convert(x, from_base, to_base))
