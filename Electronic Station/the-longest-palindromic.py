def longest_palindromic(text):
    result_first = []
    for i in range(0, len(text)):
        for j in range(0, len(text)):
            data = text[i:j+1]
            if judge_palindromic(data):
                result_first.append(data)
    len_max = max([len(buf) for buf in result_first])
    result_second = []
    for buf in result_first:
        if len(buf) == len_max:
            result_second.append(buf)
    return result_second[0]


def judge_palindromic(data):
    if len(data) in (0, 1):
        return True
    if data[0] == data[-1]:
        return judge_palindromic(data[1:-1])
    else:
        return False


if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
