import itertools

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # winner horizontally 
    for row in game:
        if all_same(row):
            print(f'Player {row[0]} is the winner horizontally')
            return True

    #vertical
    columns = [0, 1, 2]
    for col in columns:
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f'Player {row[0]} is the winner vertically')
            return True

    # winner diag (left to right)
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f'Player {row[0]} is the winner diagonally') 
        return True

    # winner diags (right to left)
    diags =[]
    cols = reversed(range(len(game)))
    rows = range(len(game))
    for col, row in  zip(cols,rows):
        diags.append(game[row][col])
    if all_same(diags):
        print('diagonal winner')
        return True
    
    return False

# setting up the board
def game_board(game_map, player=0, row=0, col=0, just_display = False):
    try:
        if game_map[row][col] != 0:
            print('The position is occupied, try again')
            return game_map, False
        print("   0  1  2")
        if not just_display:
            game[row][col] = player
        for count, row in enumerate(game):
            print(count, row)
        return game_map, True
    
    except IndexError as e:
        print('Error: make sure you input row/column as 0, 1, or 2', e)
        return game_map,False
    except Exception as e:
        print('something went very wrong', e)
        return game_map,False

play = True
players = [1,2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0,1,2): "))
            row_choice = int(input("What row do you want to play? (0,1,2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input('Game over, would you like to play again? (y,n) ')
            if again.lower() == 'y':
                print('Restarting')
            elif again.lower() == 'n':
                print('Later')
                play = False
            else:
                print('Not valid, exiting game')
                play = False