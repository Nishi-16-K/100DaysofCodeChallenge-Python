def add(n1,n2):
  return n1+n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
def subtract(n1,n2):
  return n1-n2

operations= {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}
def calc():
  logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

  print(logo)
  num1 = float(input("What's the first number: "))
  num2 = float(input("What's the second number: "))
  for i in operations:
    print(i)



  is_True = False
  while not is_True:
    opt = input("Pick an operation from the line above: ")
    result = operations[opt](num1,num2)
    print(f"{num1} {opt} {num2} = {result}")
    user = input(f"Type 'y' to continue calcualting with {result}, or type 'n' to start new calculation: ")
    if user == "n":
      is_True = True
      calc()
    else:
      num1 = result
      
