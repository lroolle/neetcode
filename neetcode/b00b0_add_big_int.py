

def add_big_int(s1, s2):
    s1, s2 = sorted([s1, s2], key=len)
    out, tmp = list(s2), 0
    for i in range(1, len(out) + 1):
        x, y = out[-i], s1[-i] if i <= len(s1) else 0
        _sum = int(x) + int(y) + tmp
        out[-i] = str(_sum)[-1]
        tmp = 0
        if _sum >= 10:
            tmp = 1

    out = ''.join(out)
    if tmp == 1:
        out = '1' + out

    return out


def bad_add_big_int(s1, s2):
    s1, s2 = sorted([s1, s2], key=len)
    out, tmp = '', 0
    for i in range(1, len(s2) + 1):
        x, y = s2[-i], s1[-i] if i <= len(s1) else 0
        _sum = int(x) + int(y) + tmp
        out += str(_sum)[-1]
        tmp = 0
        if _sum >= 10:
            tmp = 1

    if tmp == 1:
        out += '1'

    return out[::-1]


if __name__ == '__main__':
    print(add_big_int('999999999', '1'))

