def takeInput():
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))
  operate = input("Enter the operator to be used (+,-,*,/): ")
  return num1,num2,operate
a,b,operator = takeInput()

def displayResult(a,b,operator):
  if operator == '+':
    output = a + b
    print(f"Result : {a} + {b} = {output}")
  elif operator == '-':
    output = a - b
    print(f"Result : {a} - {b} = {output}")
  elif operator == '*':
    output = a * b
    print(f"Result : {a} * {b} = {output}")
  elif operator == "/":
    output = a / b
    print(f"Result : {a} / {b} = {output}")
  else:
    print("Operator incorrect!")
    
displayResult(a,b,operator)
