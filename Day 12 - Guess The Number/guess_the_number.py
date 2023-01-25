#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
from art import logo

print(logo)
print("Welome to the Utimate Guess the Number Game!!")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer agains guess. Returns the number of turns remaining."""
  if guess > answer: 
    print("Too high.")
    return turns -1
  elif guess < answer:
    print("Too low.")
    return turns -1
  else:
    print(f"You got that right!!!! The answer is {answer}.")

#Make a function to set difficulty.
def set_difficulty():
  level = input("Choose your difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
   return EASY_LEVEL_TURNS
  else:
   return HARD_LEVEL_TURNS

def game():  
  #Choosing a random number between 1 and 100.
  print("Choose a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Yooooo, the correct answer is {answer}")
  
  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to the guess the correct number.")
    #Let the user guess a number.
    guess = int(input("Guess a number: "))

#Track number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, YOU LOSE!")
      return
    elif guess != answer:
      print("Guess again.")

game()