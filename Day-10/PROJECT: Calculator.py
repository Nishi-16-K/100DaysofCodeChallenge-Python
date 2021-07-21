from art import logo

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
  print(logo)
  num1 = float(input("What's the first number: ")) 
  for i in operations:
    print(i)

  is_True = False
  while not is_True:
    opt = input("Pick an operation from the line above: ")
    num2 = float(input("Pick another number: "))
    result = operations[opt](num1,num2)

    print(f"{num1} {opt} {num2} = {result}")
    
    user = input(f"Type 'y' to continue calcualting with {result}, or type 'n' to start new calculation: ")
    if user == "n":
      is_True = True
      calc()
    else:
      num1 = result
      
calc()   
    

    
    
