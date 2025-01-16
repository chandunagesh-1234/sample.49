def add_three_numbers(num1, num2, num3):
  """
  This function adds three numbers together.

  Args:
    num1: The first number.
    num2: The second number.
    num3: The third number.

  Returns:
    The sum of the three numbers.
  """
  return num1 + num2 + num3

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate the sum
sum_of_numbers = add_three_numbers(num1, num2, num3)

# Print the result
print("The sum of the three numbers is:", sum_of_numbers)
