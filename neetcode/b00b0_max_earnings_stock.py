

def max_earnings(l):
    ret = l[1] - l[0]
    _min = min(l[1], l[0])
    for i in l:
        tmp = i - _min
        if tmp > ret:
            ret = tmp
        if _min > i:
            _min = i

    return ret


l = [9, 17, 5, 3, 4, 4, 8, 2, 4, 5, 11, 8]

print(max_earnings(l))

