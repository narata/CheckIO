# def checkio(number):
#     list_num = decomposition_factor(number)
#     if list_num:
#         result = list_split(list_num)
#         return sorted([int(buf) for buf in result])[0]
#     else:
#         return 0


# def judge_end(list_num):
#     list_num = sorted(list_num)
#     if len(list_num) == 1 or list_num[0] * list_num[1] >= 10:
#         return True
#     else:
#         return False


# def list_split(list_num):
#     result = []
#     if not judge_end(list_num):
#         for i in range(0, len(list_num) - 1):
#             for j in range(i + 1, len(list_num)):
#                 if list_num[i] * list_num[j] < 10:
#                     buf = list_num.copy()
#                     buf_1 = []
#                     for k in range(0, len(buf)):
#                         if k not in (i, j):
#                             buf_1.append(buf[k])
#                     buf_1.append(buf[i]*buf[j])
#                     result += list_split(buf_1)
#     else:
#         list_num = sorted(list_num)
#         result.append(str(list_num).replace('[', '').replace(']', '').replace(',', '').replace(' ', ''))
#     return result
    
    
# def decomposition_factor(number):
#     result = []
#     while number != 1:
#         judge = 0
#         for i in range(2, 10):
#             if number % i == 0:
#                 judge = 1
#                 result.append(i)
#                 number = number // i
#                 break
#         if judge == 0 and number >= 10:
#             return False
#     return result


def checkio(number):
    list_num = decomposition_factor(number)
    if list_num:
        list_num = sorted(list_num)
        return int(str(list_num).replace('[', '').replace(']', '').replace(',', '').replace(' ', ''))
    else:
        return 0


def decomposition_factor(number):
    result = []
    while number != 1:
        judge = 0
        for i in range(9, 1, -1):
            if number % i == 0:
                judge = 1
                result.append(i)
                number = number // i
                break
        if judge == 0 and number >= 10:
            return False
    return result


if __name__ == '__main__':
    # print(decomposition_factor(1200))
    # print(checkio(20))
    # print(judge_end([2, 2, 6]))
    # result = list_split([2, 2, 2, 3, 5])
    # print(sorted([int(buf) for buf in result])[0])
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"

