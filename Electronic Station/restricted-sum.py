def checkio(data):
    if len(data) > 1:
        return data[0] + checkio(data[1:])
    else:
        return data[0]


if __name__ == '__main__':
    print(checkio([1, 2, 3]))