import sys

def compute(x, y):
    buf_1 = 1
    buf_2 = 1
    for i in range(x, x-y, -1):
        buf_1 *= i
    for j in range(1, y+1):
        buf_2 *= j
    return int(buf_1/buf_2)
        

if __name__ == '__main__':
    K = int(sys.stdin.readline().strip())
    two = sys.stdin.readline().strip()
    A, X, B, Y = list(map(int, two.split()))
    result = []
    for i in range(0, int(K/A)+1):
        for j in range(0, int((K-A*i)/B)+1):
            if A*i+B*j == K:
                result.append([i, j])
    result_num = 0
    for buf in result:
        result_num += compute(X, buf[0]) * compute(Y, buf[1])
    print(result_num % 1000000007)
