def checkio(str_number, radix):
    letter_list = [ord(x)-55 if 'A' <= x <= 'z' else int(x) for x in list(str_number)]
    if False not in [x < radix for x in letter_list]:
        result = 0
        for i in range(len(letter_list)-1, -1, -1):
            result += letter_list[len(letter_list)-1-i] * pow(radix, i)
        return result
    return -1


if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
