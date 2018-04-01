# coding: utf-8
import itertools


def checkio(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            # 上
            if 3 <= i and matrix[i][j] == matrix[i-1][j] == matrix[i-2][j] == matrix[i-3][j]:
                return True
            # 下
            if i <= len(matrix) - 4 and matrix[i][j] == matrix[i+1][j] == matrix[i+2][j] == matrix[i+3][j]:
                return True
            # 左
            if j >= 3 and matrix[i][j] == matrix[i][j-1] == matrix[i][j-2] == matrix[i][j-3]:
                return True
            # 右
            if j <= len(matrix) - 4 and matrix[i][j] == matrix[i][j+1] == matrix[i][j+2] == matrix[i][j+3]:
                return True
            # 左上
            if i >= 3 and j >= 3 and matrix[i][j] == matrix[i-1][j-1] == matrix[i-2][j-2] == matrix[i-3][j-3]:
                return True
            # 右上
            if i >= 3 and j <= len(matrix) - 4 and matrix[i][j] == matrix[i-1][j+1] == matrix[i-2][j+2] == matrix[i-3][j+3]:
                return True
            # 左下
            if i <= len(matrix) - 4 and j >= 4 and matrix[i][j] == matrix[i+1][j-1] == matrix[i+2][j-2] == matrix[i+3][j-3]:
                return True
            # 右下
            if i <= len(matrix) - 4 and j <= len(matrix) - 4 and matrix[i][j] == matrix[i-1][j-1] == matrix[i-2][j-2] == matrix[i-3][j-3]:
                return True
    return False
    
    # a = [''.join([str(buf) for buf in data]) for data in matrix]
    # print([[''.join(y) for x, y in itertools.groupby(data)] for data in a])

if __name__ == '__main__':
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
