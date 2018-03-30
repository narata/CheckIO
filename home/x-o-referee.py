def checkio(game_result):
    for i in range(0, 3):
        if game_result[i][0] == game_result[i][1] and game_result[i][0] == game_result[i][2]:
            if not game_result[i][0] == '.':
                return game_result[i][0]
        if game_result[0][i] == game_result[1][i] and game_result[0][i] == game_result[2][i]:
            if not game_result[0][i] == '.':
                return game_result[0][i]
    
    if game_result[0][0] == game_result[1][1] == game_result[2][2]:
        if not game_result[0][0] == '.':
            return game_result[0][0]
    if game_result[2][0] == game_result[1][1] == game_result[0][2]:
        if not game_result[2][0] == '.':
            return game_result[2][0]

    return "D"

if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

