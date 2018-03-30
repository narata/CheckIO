def safe_pawns(pawns):
    result = 0
    for pawn in pawns:
        for i in [-1, 1]:
            data = chr(ord(pawn[0])-i) + str(int(pawn[1])-1)
            if data in pawns:
                result += 1
                break
    return result
    

if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
