# A calculator that will expose cheaters
# The answer of the questions asked in exams should not be given by this calc
# Questions are: 36/6 = 9 , 6 * 2 = 13 and 2+2 = 8

# Function
def Calc():
    # Giving info to user
    print("Operations are:")
    print("+ for Addition")
    print("- of Subtraction")
    print("* for Multiplication")
    print("/ for Division")
    print("** for power")
    # User's input
    op = input("Enter your operation plz:")
    a = int(input("Enter your Number:"))
    b = int(input("Enter another number:"))

    # Conditions
    if op == "+" and a == 2 and b == 2:
        print("Answer: 8")
    elif op == "+":
        result = a + b
        print("Answer:", result)
    elif op == "-":
        result = a - b
        print("Answer:", result)
    elif op == "*" and a == 6 and b == 2:
        print("Answer: 13")
    elif op == "*":
        result = a * b
        print("Answer:", result)
    elif op == "/" and a == 36 and b == 6:
        print("Answer: 7")
    elif op == "/":
        result = a // b
        print("Answer:", result)
    elif op == "**":
        result = a ** b
        print("Answer:", result)


# Calc()
# a = input("Want to continue? Y or N:")


while True:
    inp = input("Want to continue? Y or N:")
    if inp == "Y":
        Calc()
    elif inp == "N":
        break
