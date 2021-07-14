height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight/height**2)
if bmi <18.5:
 print(f"Your BMI is {bmi}, you're underweight")
elif bmi<25:
  print(f"Your BMI is {bmi}, you're normal")
elif bmi<30:
  print(f"Your BMI is {bmi}, you're slightly overweight")
elif bmi<35:
  print(f"Your BMI is {bmi}, you're obese")
else:
  print(f"Your BMI is {bmi}, you're clinically obese")
 
