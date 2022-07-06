import random

def play():
    user_choice = input("Choose 'r' for rock, 'p' for paper, 's' for scissors: \n")
    ai_choice = random.choice(['r', 'p', 's'])
    
    if user_choice == ai_choice:
        print('It is a tie')
    elif is_win(user_choice, ai_choice):
        print('You won')
    else:
        print('You lost')

def is_win(player, opponent):
    # return true if the player wins
    if (player == 'r' and opponent =='s') or (player == 's' and opponent =='p') or (player == 'p' and opponent =='r'):
        return True   

play()