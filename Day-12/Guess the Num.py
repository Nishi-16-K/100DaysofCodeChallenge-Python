import random

logo = """ 

   ____     _   _ U _____ u ____    ____          _   _       _   _   __  __     ____  U _____ u   ____        
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u      | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u     
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/      <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/     
 | |_| |   | |_| | | |___  u___) | u___) |      U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <       
  \____|  <<\___/  |_____| |____/>>|____/>>      |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\      
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)     ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_     
 (__)__)     (__) (__) (__)(__)    (__)          (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__)    

""" 
print(logo)
print("|--------- Welcome to the Number Guessing Game--------|\n"
)
print("You've to guess a number between 1 to 100")

set_num = random.randint(1,100)
user = input("Choose the difficulty level. Type easy or hard : ")

def output(chance):
  is_True = False
  while not is_True:
    print(f"You have {chance} attempts remaining to guess the number.")
    chance-=1
    user_num = int(input("Make a guess: "))
 
    if user_num > set_num:
      print("Too High.\nGuess Again.\n")
    elif user_num < set_num:
      print("Too Low. \nGuess Again.\n")
    else:
      is_True = True
      print(f"\n|---You guessed it right. It's {user_num}. You won!!---|")
    if chance == 0:
      print("\n|---You've run out of guesses. You lose!!---|")
      is_True = True


if user == "easy":
  output(10)
elif user == "hard":
  output(5)


