import collections


def popular_words(text, words):
    text = text.lower().replace(',', ' ').replace('.', ' ').replace('\n', '')
    text_dict = collections.Counter(text.split(' '))
    result = {}
    for word in words:
        if word in text_dict.keys():
            result[word] = text_dict[word]
        else:
            result[word] = 0
    return result


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
