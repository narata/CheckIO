def between_markers(text: str, begin: str, end: str) -> str:
    if text.find(begin) != -1:
        begin_index = text.find(begin)
        length = len(begin)
    else:
        begin_index = 0
        length = 0
    end_index = text.find(end) if text.find(end) != -1 else len(text)
    print(begin_index, end_index)
    return text[begin_index+length: end_index] if begin_index < end_index else ''


if __name__ == '__main__':
    print('Example:')
    print(between_markers('No[/b] hi', '[b]', '[/b]'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
