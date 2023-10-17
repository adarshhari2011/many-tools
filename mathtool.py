def square(number):
  return number*number  
def cube(number):
   return number**(1. / 3)
def root(number):
  return number**(1. / 2)
def factors(number):
  factor = []
  for i in range(1,number+1):
    if number % i == 0 :
       factor.append(i)
  return factor
def gcf(number1,number2):
  number1_factors = factors(number1)
  number2_factors = factors(number2)
  
  print(number1_factors)
  print(number2_factors)

  for i in range(len(number1_factors)-1 , 0 , -1):
    if number1_factors[i] in number2_factors:
      return number1_factors[i]
def calculator():
  opp=int(input(" Enter 1 for addtion,\n Enter 2 for subtraction,\n Enter 3 for multpication, \n Enter 4 for division,\n "))
  if opp==1:
   NUM1=float(input("Put the first number."))
   NUM2=float(input("Put the second number."))
   print("The answer is", NUM1+NUM2)

  elif opp==2:
   NUM1=float(input("Put the first number."))
   NUM2=float(input("Put the second number."))
   print("The answer is", NUM1-NUM2)

  elif opp==3:
   NUM1=float(input("Put the first number."))
   NUM2=float(input("Put the second number."))
   print("The answer is", NUM1*NUM2)

  elif opp==4:
   NUM1=float(input("Put the first number."))
   NUM2=float(input("Put the second number."))
   print("The answer is", NUM1/NUM2)