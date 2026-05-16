def fibonachi():
    a = 0
    b = 1

    while True:
        yield a
        a, b = b, a + b


count = 1

for expected in [5, 200, 1000, 100000]:
    for number in fibonachi():
        if count == expected:
            print(number)
            break
        count += 1
