from random import randint

computer_choices = {1:'rock', 2:'paper', 3:'scissor'}
players_choice = raw_input('your choice >' )
win_loose = [('scissor','paper'), ('rock','scissor'), ('paper','rock')] 
rand = computer_choices.get(randint(1,3))

def test_win_opt():
    game = (players_choice, rand)
    players_points = 0
    computers_points = 0
    print '-' * 50
    print 'computer choices' ,rand 
    print '-' * 50
    if players_choice ==rand:
        print('even')
    elif game in win_loose:
        print('Player wins')
        players_points +=1
    else:
        print('computer wins')
        computers_points += 1
    print '*' * 50

    print 'player:', players_points, 'computer:', computers_points
    

test_win_opt()
