letter_num = {'A': 0, 'D': 1, 'F': 2, 'G': 3, 'V': 4, 'X': 5}
num_letter = {0: 'A', 1: 'D', 2: 'F', 3: 'G', 4: 'V', 5: 'X'}


def encode(message, secret_alphabet, keyword):
    keyword = del_same_letter(keyword)
    adfgvx = [secret_alphabet[i*6: i*6+6]for i in range(0, 6)]
    fractionated_form = ''
    for buf in message.lower():
        data = find_station(adfgvx, buf)
        # print(data)
        if data:
            fractionated_form = fractionated_form + num_letter[data[0]] + num_letter[data[1]]
    new_table = {}
    i = 0
    while i < len(fractionated_form):
        for buf in keyword:
            if i == len(fractionated_form):
                break
            if buf in new_table.keys():
                new_table[buf] += fractionated_form[i]
                i += 1
            else:
                new_table[buf] = fractionated_form[i]
                i += 1
    result_index = sorted(new_table.keys())
    result = ''
    for buf in result_index:
        result += new_table[buf]
    return result


def decode(message, secret_alphabet, keyword):
    keyword = del_same_letter(keyword)
    print(keyword)
    adfgvx = [secret_alphabet[i * 6: i * 6 + 6] for i in range(0, 6)]
    
    i = 0
    keyword_num = {}
    while i < len(message):
        for j in keyword:
            if i >= len(message):
                break
            i += 1
            if j in keyword_num.keys():
                keyword_num[j] += 1
            else:
                keyword_num[j] = 1
    keyword_num_sort = sorted(keyword_num.items(), key=lambda item: item[0])
    
    keyword_data = {}
    i = 0
    for data in keyword_num_sort:
        keyword_data[data[0]] = message[i: i+data[1]]
        i += data[1]
    
    i = 0
    j = 0
    fractionated_form = ''
    while i < len(message):
        for buf in keyword:
            if i >= len(message):
                break
            fractionated_form += keyword_data[buf][j]
            i += 1
        j += 1
    
    result = ''
    for i in range(0, len(fractionated_form), 2):
        data = fractionated_form[i: i+2]
        result += adfgvx[letter_num[data[0]]][letter_num[data[1]]]
    return result


def find_station(adfgvx, letter):
    if 'a' <= letter <= 'z' or '0' <= letter <= '9':
        for i in range(0, 6):
            j = adfgvx[i].find(letter)
            if j != -1:
                return i, j
    return False


def del_same_letter(keyword):
    result = ''
    for buf in keyword:
        if buf not in result:
            result += buf
    return result


if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"
