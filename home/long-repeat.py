def long_repeat(line):
    if len(line) < 2:
        return len(line)
    x = 1
    result = {}
    for i in range(0, len(line)-1):
        if line[i] == line[i+1]:
            x += 1
            result[i] = x
        else:
            result[i] = x
            x = 1
    return sorted(result.items(), key=lambda item: item[1])[-1][1]


if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('abababa') == 1, "Empty"
    print('"Run" is good. How is "Check"?')
