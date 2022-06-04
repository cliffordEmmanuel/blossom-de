def getInput():
    """gets input from the user.

    Returns:
        tuple: _description_
    """

    # Basic Arithmetic 
    a = int(input("Enter first integer: ")) 
    b = int(input("Enter second integer: ")) 

    print("Enter the Arithmetic Operator") 

    operator=input(" + , - , * , /, %,: ") 

    return a, b, operator # this is a tuple..


def calculate(a:int,b:int, operator:str)->int:
    """calculates the chosen arithmetic

    Args:
        a (int): first integer
        b (int): first integer
        operator (str): chosen arithemetic operation

    Returns:
        int: result of the operation.
    """
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
    
    return answer

def main():
    a,b,operator = getInput()
    answer = calculate(a,b,operator)
    print(f"{a} {operator} {b} = {answer}")


if __name__=='__main__':
    # this is where the code begins running from.
    
    main()