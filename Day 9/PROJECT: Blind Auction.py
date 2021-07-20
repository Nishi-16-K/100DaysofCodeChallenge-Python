logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
dicti = {} 
is_true = False
while not is_true: 
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  dicti[name] = bid
  ques = input("Are there any other bidders? Type 'yes' or 'no': ")

  if ques == "no":  
    is_true = True
    high = 0
    for i in dicti:
      value = dicti[i]
      if value > high:
        high = value
        win = i
    print(f"\n|----The winner is {win} of bid {high}----|")
  else:
    print("\n")
      
  

  

