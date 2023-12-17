


import math


if __name__ == '__main__':
   print('Please think of a number between 0 and 1000 and I will have to guess it.')
   start = 0
   end = 1000
   guess_count = 0
   while start <= end:
        user_choice = ''
        next_guess = math.floor(start + end) / 2
        guess_count = guess_count + 1
        while user_choice not in ['h', 'l', 'e']:
            user_choice = input(f"My next guess is {int(next_guess)}. Press 'h' for higher, 'l' for lower. Press 'e' if I guessed it!")
        if user_choice == 'h':
           start = next_guess + 1
        elif user_choice == 'l':
           end = next_guess - 1
        else:
            print(f"Yay! I guessed in {int(guess_count)} guesses.")
            break
