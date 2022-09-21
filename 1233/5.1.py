game_list = []
name_game = input('введите название:')
while name_game != ('0'):
    if name_game in game_list:
        print('эта игра уже в списке')
    else:
        game_list.append(name_game)
    name_game = input('введите название:')
game_list.sort()
print(game_list)