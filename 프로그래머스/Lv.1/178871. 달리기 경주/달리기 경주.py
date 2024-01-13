def solution(players, callings):
    player_index = {player: idx for idx, player in enumerate(players)}
    
    for name in callings:
        box = player_index[name]
        player_index[name] -= 1
        player_index[players[box-1]] += 1
        players[box], players[box-1] = players[box-1], players[box]

    return players