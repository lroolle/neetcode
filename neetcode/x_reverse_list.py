


def recursive_reverse(l):
    if len(l) <= 1:
        return l
    return recursive_reverse(l[1:]) + [l[0]]


if __name__ == '__main__':
    print(recursive_reverse([1, 2, 3, 4]))

