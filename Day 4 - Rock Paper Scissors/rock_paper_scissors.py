rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

selection = [rock, paper, scissors]

player = int(input('Type 0 for rock, 1 for paper, or 2 for scissors to play:=> '))
if player >= 3 or player < 0:
  print("You typed an ivalid number, you LOSE!!")
else:
  print(f"You chose: {selection[player]}.")
  
  bot = random.randint(0, 2)
  print(f"Bot chose: {selection[bot]}")
  
  if player == 0 and bot == 2:
    print("Player Wins!")
  elif player == 2 and bot == 0:
    print("Player Loses!")
  elif player < bot:
    print("Bot Wins!")
  elif player > bot:
    print("Player Wins!")
  elif player == bot:
    print("It's a Tie!")