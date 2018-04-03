def checkio(data):
    data = data.replace('(', '').replace(')', '')
    data = [int(buf) for buf in data.split(',')]
    print(data)
    x1 = data[0]
    y1 = data[1]
    x2 = data[2]
    y2 = data[3]
    x3 = data[4]
    y3 = data[5]
    y0 = ((x2*x2 + y2*y2 - x1*x1 - y1*y1)*(x3-x1) - (x3*x3 + y3*y3 - x1*x1 - y1*y1)*(x2-x1))/2/((y2-y1)*(x3-x1)-(y3-y1)*(x2-x1))
    if x2-x1 != 0:
        x0 = (x2*x2+y2*y2-x1*x1-y1*y1-2*(y2-y1)*y0)/2/(x2-x1)
    else:
        x0 = (x3*x3+y3*y3-x1*x1-y1*y1-2*(y3-y1)*y0)/2/(x3-x1)
    r = pow(pow(x1-x0, 2)+pow(y1-y0, 2), 0.5)
    x0 = round(x0, 2)
    y0 = round(y0, 2)
    r = round(r, 2)
    x0 = int(x0) if x0 == int(x0) else x0
    y0 = int(y0) if y0 == int(y0) else y0
    r = int(r) if r == int(r) else r
    return "(x-{})^2+(y-{})^2={}^2".format(x0, y0, r)


if __name__ == '__main__':
    print(checkio("(9,8),(9,4),(3,6)"))
    # assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    # assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
    # assert checkio("(7,3),(9,6),(3,6)") == "(x-6)^2+(y-5.83)^2=3^2"
