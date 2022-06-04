# Basic Arithmetic 
a = int(input("Enter first integer: ")) 
b = int(input("Enter second integer: ")) 

print("Enter the Arithmetic Operator") 

operator=input(" + , - , * , /, %,: ") 

answer = None

# a+b 
if operator == '+': 
    answer = a + b 
#a-b 
elif operator == '-': 
    answer = a - b 
#a*b 
elif operator == '*': 
    answer = a * b 
#a/b 
elif operator == '/': 
    answer = a / b 
#a%b 
elif operator == '%': 
    answer = a % b 
#ab 
else: 
    print("Error message") 


print(a, operator, b, ":", answer) 