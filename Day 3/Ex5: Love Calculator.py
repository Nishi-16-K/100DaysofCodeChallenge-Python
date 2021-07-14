print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
nname = name1+name2
new_name = nname.lower()
t = new_name.count("t")
r = new_name.count("r")
u = new_name.count("u")
e = new_name.count("e")
total1 = t+r+u+e
l = new_name.count("l")
o = new_name.count("o")
v = new_name.count("v")
e = new_name.count("e")
total2 = l+o+v+e
new_total = int(str(total1)+ str(total2))
if new_total <10 and new_total>90:
  print(f"Your score is {new_total}, you go together like coke and mentos.")
elif new_total >40 and new_total<50:
 print(f"Your score is {new_total}, you're alright together.") 
else:
  print(f"Your score is {new_total}")



