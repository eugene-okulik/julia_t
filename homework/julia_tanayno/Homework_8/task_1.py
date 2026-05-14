import random

salary = int(input('Fill in salary '))
bonus = random.choice([True, False])

if bonus is True:
    result = salary + random.randint(1, 10000)
else:
    result = salary

print(f'{salary}, {bonus} - {result}')
