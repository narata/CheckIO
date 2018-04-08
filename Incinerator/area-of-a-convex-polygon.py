def checkio(data):
    if len(data) == 3:
        return area_of_triangle(data)
    else:
        return area_of_triangle(data[0: 3]) + checkio(data[0:1] + data[2:])


def area_of_triangle(points):
    a = [points[1][0]-points[0][0], points[1][1]-points[0][1]]
    b = [points[2][0]-points[0][0], points[2][1]-points[0][1]]
    # print(abs(a[0]*b[1]-b[0]*a[1])/2)
    return abs(a[0]*b[1]-b[0]*a[1])/2


if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
    assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
    assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
    assert almost_equal(checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
    assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
    assert almost_equal(checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"
