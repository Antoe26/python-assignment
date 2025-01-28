def simple_calculator():
  """
  This function performs basic arithmetic operations 
  (addition, subtraction, multiplication, and division) 
  on two user-inputted numbers.
  """
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    if operator == '+':
      result = num1 + num2
    elif operator == '-':
      result = num1 - num2
    elif operator == '*':
      result = num1 * num2
    elif operator == '/':
      if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return 
      else:
        result = num1 / num2
    else:
      print("Invalid operator. Please use +, -, *, or /.")
      return

    print(f"{num1} {operator} {num2} = {result}")

  except ValueError:
    print("Invalid input. Please enter valid numbers.")

# Run the calculator
simple_calculator()