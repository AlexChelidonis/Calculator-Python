def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def calculator():
    print("Welcome to the Python Calculator!")
    print("Operations: + for addition, - for subtraction, * for multiplication, / for division")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            op = input("Enter an operator (+, -, *, /): ").strip()
            num2 = float(input("Enter the second number: "))
            
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator. Please use +, -, *, or /.")
                continue
            
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        
        again = input("Do you want to calculate again? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    calculator()