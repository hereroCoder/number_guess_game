import random


# computer guesses user number
def computer_guess_number():
  print('The computer will be guessing your number')
  print("Think of a number")
  print("Ok now i will try to guess it.")
  count  = 0
  lower_limit = 1
  upper_limit = 100
  computer_guess = random.randint(lower_limit,upper_limit)
  while count < 10:
    reponse = input (f'Is the number {computer_guess}? y/n ').lower()
    if reponse == 'y':
      print(f'Yay im good at this!! So your number was {computer_guess}')
      if count <=5:
        print(f"I think i was pretty fast, took me {count} gueses")
      else:
        print(f"That was a tough win, took me {count} gueses")
      break
    elif reponse == 'n':
      hint = input('Oh thats a bummer, should i guess higher (h) or lower(l)').lower()
      if hint == 'l':
        upper_limit = computer_guess
        computer_guess = random.randint(lower_limit, upper_limit)
      elif hint == 'h':
        lower_limit = computer_guess
        computer_guess = random.randint(lower_limit, upper_limit)
      else:
        print('Please give me a hint if i should guess higher (h) or lower (l)')
      count += 1
    else:
      print('y/n did i guess the numer correctly?')
  else:
    print("Thats me giving up, i tried 10 times")


#user guesses computer number
def user_guess_number():
  print('You will be guessing the computer number')
  print("You only have 10 chances and I will be giving you hints")
  print("Here you go!\n")
  number = random.randint(1,100)
  count = 1
  while count <= 10:
    the_guess = int(input("Guess the number: "))
    if the_guess == number:
      print(f"Nice! That is correct. The number was {number}")
      if count <=5:
        print(f"I think i was pretty fast, took you {count} gueses")
      else:
        print(f"That was a tough win, took you {count} gueses")
      break
    elif the_guess > number:
      print("Try something lower")
    elif the_guess < number:
      print("Nope, Higher")
    count +=1
  else:
    print(f"Game over!! You lost :(). Number was {number}")


def game():
  game_trials = 3
  while game_trials > 0:
    try:
      print("Modes: press 1 or 2")
      mode = int(input('which mode do you want? '))

      if mode == 1:
        computer_guess_number()

      elif mode == 2:
        user_guess_number()

      else:
        print('Sorry that was invalid,press 1 or 2 to select game mode \n')

    except:
      print('I am confused, i think you pressed an invalid character. Please try again and input numbers \n')

    game_trials -= 1

  else:
    print('You can start the game again anytime')
    print('Alright! i will see you next time')

game()
