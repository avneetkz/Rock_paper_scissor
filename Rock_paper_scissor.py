# Headline of the game 

print("\n WELCOME TO ROCK PAPER SCISSOR GAME \n")
print("You are Player 1 \n")

# importing random module 
import random

user1= input("Choose from Rock, Paper and Scissor: ").lower()
user2= random.choice(["Rock", "Paper", "Scissor"]).lower()

print(f'Player 2 have chosen {user2}')

# defining conditions

if user1 == 'rock' and user2 == 'paper':
    print("Player 2 won !")
elif user1 == 'paper' and user2 == 'scissor':
    print("Player 2 won !")
elif user1 == 'scissor' and user2 == 'rock':
    print("Player 2 won !")
elif user1 == user2:
    print("It's a TIE.. ")
else:
    print("Player 1 won !")
