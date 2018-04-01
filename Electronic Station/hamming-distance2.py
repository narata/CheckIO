def checkio(n, m):
    list_m = list(str(bin(m))[2:])
    list_n = list(str(bin(n))[2:])
    result = 0
    for i in range(0, len(list_m) if len(list_m) > len(list_n) else len(list_n)):
        data_m = int(list_m.pop()) if len(list_m) > 0 else 0
        data_n = int(list_n.pop()) if len(list_n) > 0 else 0
        if data_m + data_n == 1:
            result += 1
    return result
    


if __name__ == '__main__':
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
