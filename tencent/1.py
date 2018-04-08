# coding:utf8

import sys

if __name__ == '__main__':
    for line in sys.stdin:
        a = line.split()
        n = int(a[0])
        m = int(a[1])
        print(int(m*n/2))
