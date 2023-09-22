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
    i = x.index('.') - 1
    for c in list(x):  # 123.43
        if c != '.':
            d = digits[c]
            res += d * (b ** i)
            i -= 1
    return res


def to_custom_base(x, b, prec=8):  # вопрос?? можно ирр. x?
    # Получим b-разложение x
    k = math.floor(math.log(x, b)) + 1
    # Минимальная степень, в которую нужно
    # возвести b, чтобы получилось число больше x
    res = ""
    for i in range(k - 1, -prec - 1, -1):
        digit = math.floor((x / (b ** i)) % b)  # целую часть текущей цифры
        x -= digit * (b ** i)
        res += ('.' + str(digit) if len(res) == k else str(digit))
    return res


from_base = int(input('Из СИ: '))
to_base = int(input('В СИ: '))
x = input('Число: ')
print(to_custom_base(from_custom_base(x, from_base), to_base))
