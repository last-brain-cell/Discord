
def calc(x: int, y: int, operator: str):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y
    elif operator == '%':
        return x % y
    else:
        return "operator not supported"
