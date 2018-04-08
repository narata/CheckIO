# def probability(dice_number, sides, target):
#     if dice_number * sides < target:
#         return 0
#     if dice_number == 1:
#         if target <= sides and target != 0:
#             return 1/sides
#         else:
#             return 0
#     else:
#         result = 0
#         range_num = target if target < sides else sides+1
#         for i in range(1, range_num):
#             if dice_number == 10:
#                 print(i)
#             result += (1/sides)*probability(dice_number-1, sides, target-i)
#     # print(result)
#     return round(result, 4)


def probability(dice_number, sides, target):
    result = 0
    point_list = [(1, n) for n in range(1, sides+1)]
    buf_list = point_list.copy()
    for i in range(1, dice_number):
        buf_list = multi_list(buf_list, point_list)
    # print(buf_list)
    for x in buf_list:
        if x[1] == target:
            result = x[0]/pow(sides, dice_number)
    # print(result)
    return result
    

def multi_list(list_1, list_2):
    result = []
    for i in list_1:
        for j in list_2:
            result.append((i[0]*j[0], i[1]+j[1]))
    # print(result)
    end_result = list(set([(0, x[1]) for x in result]))
    # print(result)
    # print(end_result)
    for buf in result:
        end_result = [(x[0]+buf[0], x[1]) if x[1] == buf[1] else x for x in end_result]
    return end_result
    

if __name__ == '__main__':
    
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
    # assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    # assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    # assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    # assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    # assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
