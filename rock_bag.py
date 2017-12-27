from random import randint
slump = {1:'rock', 2:'paper', 3:'scissor'}
loose_options = [('scissor','paper'), ('rock','scissor'), ('paper','rock')] 
slumpen = slump.get(randint(1,3))
player_inp = raw_input('your choice >' )
def test_win_opt():
    player_choice = player_inp
    game = (player_choice, slumpen)

    print '-' * 50
    print player_choice, 'players choice'
    print slumpen, 'computers choice'
    print '*' * 50
    print game, 'game'

    if player_choice == slumpen:
        print('even')
    elif game in loose_options:
        print('Player wins')
    else:
        print('computer wins')

test_win_opt()
