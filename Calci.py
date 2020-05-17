
num1 = float(input("Enter first number: "))
oper= input("Enter the operator: ")
num2 = float(input("Enter second number: "))

if oper == "+" :
    print(num1+num2)
elif oper == "-" :
    print(num1-num2)
elif oper == "*" :
    print (num1*num2)
elif oper == "/" :
    print (num1/num2)
elif oper == "%" :
    print (num1%num2)
else :
    print ("Invalid Operator")

