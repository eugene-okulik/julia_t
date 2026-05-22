def calc_decorator(func):
    def wrapper(*args):
        first = args[0]
        second = args[1]
        if first < 0 or second < 0:
            return func(first, second, '*')
        elif first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        else:
            return func(first, second, '/')
    return wrapper


@calc_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
print(calc(first, second))
