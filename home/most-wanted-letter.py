import re


def checkio(text):
    text = text.lower()
    buf = re.findall('[a-zA-z]', text)
    result = {}
    for letter in buf:
        if letter not in result.keys():
            result[letter] = 1
        else:
            result[letter] += 1
    result = sorted(result.items(), key=lambda item:item[1], reverse=True)
    letters = []
    num = result[0][1]
    for buf in result:
        if buf[1] == num:
            letters.append(buf[0])
    print sorted(letters)[0]
    return sorted(letters)[0]
    # replace this for solution
    # return 'a'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")