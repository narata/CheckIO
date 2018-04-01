import functools


def checkio(number):
    buf = list(str(number).replace('0', ''))
    # if len(buf) < 2:
    #     return int(buf[0])
    return functools.reduce(lambda x, y=1: int(x) * int(y), buf)


if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
