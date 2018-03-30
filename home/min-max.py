import collections


def min(*args, **kwargs):
    args = args[0] if len(args) == 1 else args
    if not isinstance(args, collections.Iterable):
        return args
    args = [buf for buf in args]
    key = kwargs.get("key", None)
    if key is not None:
        args_later = [key(buf) for buf in args]
    else:
        args_later = args
    result = args[0]
    result_later = args_later[0]
    for i in range(1, len(args)):
        if args_later[i] < result_later:
            result = args[i]
            result_later = args_later[i]
    return result


def max(*args, **kwargs):
    args = args[0] if len(args) == 1 else args
    if not isinstance(args, collections.Iterable):
        return args
    args = [buf for buf in args]
    key = kwargs.get("key", None)
    if key is not None:
        args_later = [key(buf) for buf in args]
    else:
        args_later = args
    result = args[0]
    result_later = args_later[0]
    for i in range(1, len(args)):
        if args_later[i] > result_later:
            result = args[i]
            result_later = args_later[i]
    return result


if __name__ == '__main__':
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")