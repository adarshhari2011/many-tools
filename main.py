import healthtool, mathtool, random_tool, finance

print("Welcome to Many tools")
first=int(input("Press 1 to use Math Tools\n Press 2 to use Health Tools\nPress 3 to use Finance Tools\n Press 5 to use Random Tools"))
if first == (1):
  print("Welcome to Math Tools")
  math_tool=int(input("Press 1 to use GCF\n Press 2 to use Factors of a Number\n Press 3 to use Roots of a Number\n Press 4 to use Square of a Number\n Press 5 to use a Calulator\n Press 6 to use Cube of a Number"))
  if math_tool == 1:
    number1=int(input("Enter the first number"))
    number2=int(input("Enter the second number"))
    print(mathtool.gcf(number1, number2))
  elif math_tool == 2:
    print(mathtool.factors(10))
  elif math_tool == 3:
    number = int(input("Enter a number : "))
    print(mathtool.root(number))
  elif math_tool == 4:
    print(mathtool.square(9))
  elif math_tool == 5:
    mathtool.calculator()
  elif math_tool == 6:
    print(mathtool.cube(7))
elif first ==
print(healthtool.bmi(50, 3))
print(healthtool.lb_to_kg(150))
print(healthtool.kg_to_lb(150))
print(healthtool.cm_to_in(137))
print(healthtool.in_to_cm(137))
print(healthtool.blood_pressure_high_low(120))
print(healthtool.blood_pressure_high_low(140))
# Finance
print(finance.simple_interest(15, 100, 10))
print(finance.compound_intrest(20, 10, 2))
# Random
print(random_tool.password(2,1,10))
random_tool.username()
print(random_tool.dice_throw())
print(random_tool.toss())
print(random_tool.cards())