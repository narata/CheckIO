def checkio(expression):
    bracket = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for buf in expression:
        if buf in '({[':
            stack.append(buf)
        if buf in '}])':
            if len(stack) == 0 or buf != bracket[stack.pop()]:
                return False
    return True if len(stack) == 0 else False


if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
