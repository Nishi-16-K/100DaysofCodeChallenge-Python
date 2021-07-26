import random

from game_data import data
from art import logo
from art import vs
def user():
  choice = random.choice(data) 
  global name, description, country, follower
  name = choice["name"]
  description = choice["description"]
  country = choice["country"]
  follower = choice["follower_count"]

print(logo)  
random1 = user()
is_True = False
score = 0

while not is_True:
  A = print(f"COMPARE A: {name}, a {description}, from {country}")  
  A_fol = follower
  random2 = user()
  print(vs)
  B = print(f"AGAINST B: {name}, a {description}, from {country}")
  B_fol = follower
  

  u_choice = input("\nWho has more followers? Type 'A'or 'B': ")
  if u_choice == 'A':
    if A_fol > B_fol:
      score += 1
      print(f"\n|---You're right. Currrent score: {score} 🥳---|\n")
      random1 = random2      
    else:
      print(f"\n|---Sorry that's wrong 😭. You lose at score {score}---|\n")
      is_True = True
  elif u_choice == 'B':
    if B_fol > A_fol:
      score += 1
      print(f"\n|--You're right. Currrent score: {score} 🥳---|\n")
      random1 = random2
    else:
      print(f"\n|--Sorry that's wrong 😭. You lose at score {score}--|\n")
      is_True = True
