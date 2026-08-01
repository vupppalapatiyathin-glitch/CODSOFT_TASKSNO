# SIMPLE CALCULATOR BY PYTHON

num1 = int(input("Give 1st number:"))
num2 = int(input("Give 2nd number:"))
operator = input("give operator")
if operator == "+":
    print(f"Addition of 2 numbers {num1 + num2}")
elif operator == "-":
    print(f"Subtraction of 2 numbers {num1 - num2}")
elif operator == "*":
    print(f"Multiplication of 2 numbers {num1 * num2}")
elif operator == "/":
    print(f"Division of 2 numbers {num1/ num2}")
else:
    print("operator")