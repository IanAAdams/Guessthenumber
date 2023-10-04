import random
from art import header
print(header)

print("\nWelcome to the number guessing game!")
print("Im thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  guesses = 10
elif difficulty == "hard":
  guesses = 5

computer_guess = random.randint(1, 100)
is_game_over = False

while not is_game_over:
  if guesses != 0:
    print(f"You have {guesses} attemps remaining to guess the number.")
    user_guess = int(input("Make a guess:\n"))
    if user_guess > computer_guess:
      print("Too high.")
      print("Guess again.")
    elif user_guess < computer_guess:
      print("Too low.")
      print("Guess again.")
    else:
      print(f"You got it! The answer is {computer_guess}")
      is_game_over = True
    guesses -= 1
  else:
    is_game_over = True
    print(f"SIKEEEE!!! You ran out of guesses. The number was {computer_guess}. You Lose!")