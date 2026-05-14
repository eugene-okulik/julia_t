number = 55

while True:
    user_input = int(input('Enter a number: '))
    if user_input != number:
        print('Попробуйте снова')
        continue
    else:
        print('Поздравляю! Вы угадали!')
        break
