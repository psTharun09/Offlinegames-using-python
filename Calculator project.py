import art

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {"+": add, "-": sub, "*": mul, "/": div}
# result=operands["+"](1,2)
# print(result)
def calculator():
    print(art.logo)
    a = float(input("Type the first number:"))
    continues = True
    while continues:
        operation = input("+\n-\n*\n/\nPick an operation:")
        b = float(input("Type the second number:"))
        result = operations[operation](a, b)
        print(f'{a}{operation}{b}={result}')
        y_or_n = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:").lower()
        if y_or_n == "y":
            a = result
        elif y_or_n == "n":
            continues = False
            calculator()


calculator()
