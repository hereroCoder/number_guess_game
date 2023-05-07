import random
import time

# number guessing game
# user chooses to either guess the computer number
# or Computer guess the number user is thinking

def user_guess_number():
  number = random.randint(1, 100)

  count = 1
  guess = None

  print('im choosing a random number then will see if you can guess it')
  time.sleep(3)
  print('choosing.....hold on im shuffling')
  time.sleep(3)
  print('Ok got it!')

  while guess != number:
      guess = int(input('Guess a number between 1 and 100: '))
      time.sleep(0.5)
      if guess == number:
          break
      else:
          if guess > number:
              print('wrong, try something lower')
          else:
              print('wrong, try something higher')
      count += 1

  print(f'Congratulations! The correct number was {number}')
  print(f'it took you {count} guesses')
  # used a for loop to give the user 3 tries
  # but changed to while loop so they can keep guessing until right
  # introducing the time library for pauses makes this more interesting
  # Even though it makes the program slower its adding life to it


def computer_guess_number():
  print("Let me guess the number you are thinking. I will try to do it in 10 trials")


  print("You will give me hits if i should go lower or higher")
  print("")
  print("Lets Begin")
  print("")
  print("Think of a number between 0 and 100")
  print("")

  trials = 10
  low = 0
  high = 100


  while trials > 0:
      number = random.randint(low, high)
      print("I guessed {}".format(number))
      clue = input(
          "Is that the correct number(c) or lower(l) or upper(u)").lower()

      if clue == 'c':
          print("Yay i guess the number {} correctly".format(number))
          break
      elif clue == 'l':
          high = number - 1
      elif clue == 'u':
          low = number + 1
      else:
          print("Sorry that was an invalid input")

      trials -= 1
  else:
        print("Unfortunately i didnt guess correctly after 10 trials")


def playing():
  user = input("1. Do you want to guess the number 2. Do you want the computer to guess your number ")
  if user == "1":
    user_guess_number()
  elif user == "2":
    computer_guess_number()
  else:
    print("Invalid! please select 1 or 2")

playing()