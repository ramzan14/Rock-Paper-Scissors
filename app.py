import random
choice = ['rock', 'paper', 'scissors']
play_again = True

while play_again:
    user_input = str(input("Choose your play: \n"))
    
    try:
        user_input = choice.index(user_input)
    except:
        print("Please make sure you chose the right option.")
        break

    computer = random.randint(0,2)
    win = (computer - user_input) % 3
    if win == 0:
        print(f"Its a tie, computer and you chose {choice[user_input]}")
    elif win == 1:
        print(f"Computer won, Computer chose {choice[computer]}, You chose {choice[user_input]}.")
    else:
        print(f"You won, You chose {choice[user_input]} and Computer chose {choice[computer]}.")
    ch = str(input("Do you wanna play more?(Y/N) \n"))
    if  ch == 'n' or ch == 'N':
        break

print("Thanks for playing. See you next time.")
