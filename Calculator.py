#making a calculator using python
num1= float(input("Enter the first number: "))
op= input("Enter the operator of your choice: ")
num2= float(input("Enter the second number: "))

if op == "+":
    print(num1+num2)
elif op =="-":
    print(num1-num2)
elif op =="*":
    print(num1*num2)
elif op =="/":
    print(num1/num2)
elif op =="%":
    print(num1%num2)
else:
    print("invalid operator")
