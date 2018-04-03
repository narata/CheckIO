import itertools


def largest_histogram(histogram):
    result = []
    for i in range(1, max(histogram)+1):
        list_buf = [str(1) if buf-i >= 0 else str(0) for buf in histogram]
        list_group = [''.join(y) for x, y in itertools.groupby(list_buf)]
        list_group_len = [len(buf) if '1' in buf else 0 for buf in list_group]
        result.append(max(list_group_len) * i)
    print(result)
    return max(result)


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert largest_histogram([5]) == 5, "one is always the biggest"
    # assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    # assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    # assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
