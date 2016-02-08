def checkio(game_results):
    for row in game_results:
        print(row[0])
        if row[0]==row[1] ==row[2] and row[0] != '.' :





result=checkio(["XXO","XXO","XOO"])
print(result)