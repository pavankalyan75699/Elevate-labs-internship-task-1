def add(a,b):
    "addition of two numbers"
    return  a+b
def subtract(a,b):
    "subtraction of two numbers"
    if a>b:
        return a-b
    else:
       return -(b-a)
def multiply(a,b):
    "multiplication of two numbers"
    return  a*b
def division(a,b):
    "division of two numbers"
    if b!=0:
        return  a/b
    else:
        return "infinite"
    
def calculator():
    print("=== welcome to  CLI(command line interface) Calculator ===")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit.\n")

    while True:
        # Take operator input
        option = input("Enter operation (+, -, *, /) or 'exit' to quit: ").strip().lower()

        if option == "exit":
            print("Exiting Calculator... Goodbye!")
            break

        if option not in ['+', '-', '*', '/']:
            print("Invalid operation! Please try again.\n")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")
            continue

        # Perform calculation
        if option == '+':
            result = add(num1, num2)
        elif option == '-':
            result = subtract(num1, num2)
        elif option == '*':
            result = multiply(num1, num2)
        elif option == '/':
            result = division(num1, num2)

        print(f"Result: {result}\n")


if __name__ == "__main__":
    calculator()