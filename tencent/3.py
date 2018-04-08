import sys

if __name__ == '__main__':
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    computer = [list(map(int, sys.stdin.readline().strip().split())) for i in range(0, n)]
    task = [list(map(int, sys.stdin.readline().strip().split())) for i in range(0, m)]
    result = []
    for task_buf in task:
        computer_choose = [0, 1000]
        computer_choose_num = -1
        for computer_buf in computer:
            if computer_buf[0] >= task_buf[0] and computer_buf[0]>= task_buf:
                if
