import random

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
image = [rock,paper,scissors]
user_choice = int(input("Welcome to the game!! Which one you wanna choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))

if user_choice >= 3 or user_choice <0:
  print("Invalid number")
else:
  print(image[user_choice])

  comp_choice = random.randint(0,2)
  print(f"Computer choose: ")
  print(image[comp_choice])

  if user_choice == 0 and comp_choice == 2:
    print("You win!!") 
  elif user_choice == 2 and comp_choice == 0:
    print("You lose!!") 
  elif user_choice < comp_choice:
    print("You lose")
  elif user_choice > comp_choice:
    print("You win")
  elif user_choice == comp_choice:
    print("It's a tie")




