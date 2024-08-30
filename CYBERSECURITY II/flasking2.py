def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate(calc, n1, n2):
    return calc(n1, n2)

result = calculate(add, 3, 4)
print(result)