

def recursive_reverse(s):
    if len(s) <= 1:
        return s
    return recursive_reverse(s[1:]) + s[0]


if __name__ == '__main__':
    print(recursive_reverse('abcdefg'))

