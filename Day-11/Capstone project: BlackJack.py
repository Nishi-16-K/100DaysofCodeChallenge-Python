import random
 
  logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def play():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  is_res = False
  if is_res == False:
    user = input("Do you wannna play game of blackjack? Type 'y' for yes and 'n' for no: ")
    if user == "y":
      is_res = False
      print(logo)
      def output():
        my_card = []
        comp_card = []
        my_card += random.sample(cards,2)
        my_score = sum(my_card)
        print(f" Your card: {my_card}, current score: {my_score}")

        comp_card = random.sample(cards,2)
        comp_score = comp_card[0] + comp_card[1]
        print(f" Computers first card: {comp_card[0]}")
        is_True = False
        while is_True ==False:  
          ans = input("Type 'y' for another card, type 'n' to pass: ")
      
          if ans == 'y':
            my_card.append(random.choice(cards))
            my_score = sum(my_card)
            print(f" Your card: {my_card}, current score: {my_score}")  
            comp_card.append(random.choice(cards))
            comp_score = sum(comp_card)
            print(f" Computers first card: {comp_card[0]}")
            if my_score > 21:
              print(f"Your final hand: {my_card}, final score: {my_score}")  
              print(f"Computers final hand: {comp_card}, final score: {comp_score}") 
              print("|----You went over 21. You lose 😭----|")
              is_True = True
            elif comp_score > 21:
              print(f"Your final hand: {my_card}, final score: {my_score}")  
              print(f"Computers final hand: {comp_card}, final score {comp_score}") 
              print("|----Computer went over 21. You win! 😎----|")
              is_True = True
            else:

              is_True = False
              output()
            
          
          elif ans == 'n':
            is_True = True
            print(f"Your final hand: {my_card}, final score: {my_score}")  
            print(f"Computers final hand: {comp_card}, final score {comp_score}") 
            if my_score > 21:
              print(f"Your final hand: {my_card}, final score: {my_score}")  
              print(f"Computers final hand: {comp_card}, final score {comp_score}") 
              print("|----You went over 21. You lose 😭----|")
            elif comp_score > 21:
              print(f"Your final hand: {my_card}, final score: {my_score}")  
              print(f"Computers final hand: {comp_card}, final score {comp_score}") 
              print("|----Computer went over 21. You win! 😎----|")
            else:
        
              if comp_score == my_score:
                print("|----Draw----|")
              elif my_score > comp_score:
                print("|----You win 😎----|")
              elif my_score < comp_score:
                print("|----You lose 😭----|")
              play()
      output()
  else:
    is_res = True

play()
