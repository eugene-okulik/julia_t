def fibonachi():
    a = 0
    b = 1

    while True:
        yield a
        a, b = b, a + b

# не поняла, как убрать дублирование кода ниже
# для решения задачи использовала пример с урока 8 


count = 1

for number in fibonachi():
    if count == 5:
        print(number)
        break
    count += 1

for number in fibonachi():
    if count == 200:
        print(number)
        break
    count += 1

for number in fibonachi():
    if count == 1000:
        print(number)
        break
    count += 1

for number in fibonachi():
    if count == 100000:
        print(number)
        break
    count += 1
