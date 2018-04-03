def reverse_roman(roman_string):
    num_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    i = 0
    while i < len(roman_string):
        if i < len(roman_string)-1 and num_dict[roman_string[i]] < num_dict[roman_string[i+1]]:
            result += num_dict[roman_string[i+1]]-num_dict[roman_string[i]]
            i += 2
        else:
            result += num_dict[roman_string[i]]
            i += 1
    print(result)
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');