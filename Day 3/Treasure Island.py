print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||")
print("-----HEY, WHAT'S UP? WELCOME To  TREASURE ISLAND!!--------")
print("||-||-||-||-||-||-||-||-||-||-||-||-||-||-||-||")
print("\nThe reason you're here is because you gotta find the treasure. So are you ready? Let's go!\n")
choice = input("Imagine that you are on deserted road and you have two ways in front of you. Which will you choose left or right? Type 'R' or 'L': ")
if choice == 'R':
  type = input("You have reached the pond. So do you wanna use boat or swim? Type 'B' for boat and 'S' for swim")
  if type == "B":
    hut = input("Congratulations!! You successfully crossed the lake and now you are infront of three small huts: Red, Blue and Yellow. Which one you want to enter? Type 'R' for Red, 'B' for Blue and 'Y' for Yellow: ")
    if  hut == "R":
      print("GAME OVER!! Oh no, You got attacked by the army Sorry to see you go")
    elif hut == "B":
      print("GAME OVER!! Oh no, You got bit by zombies. Sorry to see you go")
    else:
      print("Very very congratulations!! You finally reached the treasure. I am so happy for you.") 
  else:
    print("GAME OVER!! Oh no, You drowened because of depth of the lake. Sorry to see you go")
else:
 print("GAME OVER!! Oh no, You choose the  wrong way. Sorry to see you go")
