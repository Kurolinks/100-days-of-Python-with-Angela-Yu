from art import logo
from replit import clear

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number ?: "))
  
  for item in operations:
      print(item)
    
  loading = True
  while loading:
      operation_symbol = input("Pick an operation: ")
      num2 = float(input("What's the next number ?: "))
      operation_function = operations[operation_symbol]
      answer = operation_function(num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")
      calculate_again = input(
          f"type 'y' to continue calculating with {answer}, or type 'n' to exit.: "
      )
      if calculate_again == ("y"):
          num1 = answer
      elif calculate_again == ("n"):
        loading = False
        clear()
        calculator()
      else:
          loading = False

calculator()
