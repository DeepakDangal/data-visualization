def plus(n1,n2):
    print(n1+n2)
    return

def minus(n1,n2):
    print(n1-n2)
    return
def multiply(n1,n2):
    print(n1*n2)
    return
def divide(n1,n2):
    print(n1/n2)
    return

num1=int(input("first number: "))
num2=int(input("second number: "))

choice=input("""
select your function:
a. add
b. subtract
c. multiply
d. divide
""")

if choice=="a":
    print("the answer is: ",end="")
    plus(n1,n2)
elif choice=="b":
    print("the answer is: ",end="")
    minus(n1,n2)

elif choice=="c":
    print("the answer is: ",end="")
    multiply(n1,n2)
elif choice=="d":
    print("the answer is: ",end="")
    divide(n1,n2)

print(choice)





