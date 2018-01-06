from random import randint
import random

computer_choices = {1:'rock', 2:'paper', 3:'scissor'}
win_loose = [('scissor','paper'), ('rock','scissor'), ('paper','rock')] 
value = random.randint(1,3)
rand = computer_choices.get(value)

def scissor_game():
    #rand = computer_choices.get(random.randint(1,3))
    players_points = 0
    computers_points = 0
    while True:
        players_choice = raw_input('your choice >' )
        game = (players_choice, rand)
        print '-' * 50
        print 'computer choices' ,rand 
        print '-' * 50
        if players_choice ==rand:
            print('even')
        elif game in win_loose:
            print('Player wins')
            print '/' * 50
            players_points +=1
        else:
            print('computer wins')
            computers_points += 1
            print '*' * 50
    
        print 'player:', players_points, 'computer:', computers_points
        print '-' * 50
        if players_points >4:
            return False

scissor_game()
