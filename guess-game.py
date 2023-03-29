import random
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
play = input("do you want to play 'y/n':")

if (play == "y") or (play == "yes") or (play == "Yes") :
     print("Welcome to the game of guess 🤡")
     magic_number = random.randint(0,10)
     number = int(input("enter the number a number between 0 and 10 👉:"))
     if number == magic_number :
         print(f"wow you got it right💯💯🍾🍾you pick {number} and magic number was {magic_number}")
     elif abs(number - magic_number) == 1:
         print(f"You are off by one,you pick {number} and magic number {magic_number}")
     else:
         print(f"wrong guess it was {magic_number} ❌")
elif play == "n" or play == "no" or play == "No" or play == "NO":
    print("see you later")
else:
    print("Enter the correct input 🤔🥴")
