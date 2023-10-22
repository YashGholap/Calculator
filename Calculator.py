#calculator
from art import logo
print(logo)
#add function
def add(n1, n2):
    return n1 + n2

#sub function
def sub(n1, n2):
    return n1 - n2

#mul function
def mul(n1, n2):
    return n1 * n2

#div function
def div(n1, n2):
    return n1 / n2

#dictionary named operations
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
  num1 = float(input("What's the first number? : "))
  for operator in operations:
      print(operator)
  
  continue_flag = True
  while continue_flag:
      operator = input("Which operation do you want to perform? ")
  
      if operator not in operations:
          print("Invalid operator!")
          continue
  
      num2 = float(input("What's the second number? : "))
  
      op = operations[operator]
      first_answer = op(num1, num2)
      print(f"{num1} {operator} {num2} = {first_answer}")
  
      con = input(f"Type 'y' to continue with {first_answer}, or type 'n' to start with new calculation. ").lower()
  
      while con not in ['y', 'n']:
          print("Invalid input!")
          con = input(f"Type 'y' to continue with {first_answer}, or type 'n' to exit. ").lower()
  
      if con == 'n':
          continue_flag = False
          calculator()
      else:
          num1 = first_answer

calculator()