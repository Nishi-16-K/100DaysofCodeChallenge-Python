#Eazy Level - Order  randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Code:

passw = ""

for l in range(1, nr_letters + 1):
 passw = passw+random.choice(letters)

for s in range(1, nr_symbols + 1):
 passw = passw+random.choice(symbols)

for n in range(1, nr_numbers + 1):
 passw = passw+random.choice(numbers)

print("Simple Password: ",passw)



  
#Hard Level - Order of characters not randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

for l in range(1, nr_letters + 1):
  password += random.choice(letters)

for s in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for n in range(1, nr_numbers + 1):
  password += random.choice(numbers)

random.shuffle(password)


passwordstr = ""
for p in password:
  passwordstr+=p
print(f"Strong password:  {passwordstr}")
