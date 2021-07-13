two_digit_number = input("Type a two digit number: ")

#first we will check the type of two_digit_number, it will be string, and then we will cahneg it to integer type)

num1 = two_digit_number[0]
num2 = two_digit_number[1]
output = int(num1) + int(num2)
new_output = str(output)
print(num1 + "+" + num2 + "=" + new_output)
