def repeat_inside(line):
    result = []
    for i in range(2, len(line)+1):
        for j in range(0, len(line)+1-i):
            print(line[j:j+i])
            if judge_repeat(line[j:j+i]):
                result.append(line[j:j+i])
    result = sorted(result, key=lambda x: len(x), reverse=True)
    
    return result[0] if len(result) >= 1 else ''


def judge_repeat(line):
    common_divisor = []
    for i in range(1, len(line)):
        if len(line) % i == 0:
            common_divisor.append(i)
    for i in common_divisor:
        group_list = [line[j:j+i] for j in range(0, len(line), i)]
        if len(set(group_list)) == 1:
            return True
    return False


if __name__ == '__main__':
    print(repeat_inside('rghtyjdfrtdfdf56r'))
    # print(judge_repeat('dfdf'))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert repeat_inside('aaaaa') == 'aaaaa', "First"
    # assert repeat_inside('aabbff') == 'aa', "Second"
    # assert repeat_inside('aababcc') == 'abab', "Third"
    # assert repeat_inside('abc') == '', "Forth"
    # assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    # print('"Run" is good. How is "Check"?')
