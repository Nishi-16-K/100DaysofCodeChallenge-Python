def prime_checker(number):
  is_prime = True
  for i in  range(2,number):
    if number % i == 0:
      is_prime= False
  if is_prime:
    print("It is prime number")
  else:
    print("It is non prime number")

n = int(input("Check this number: "))
prime_checker(number=n)
