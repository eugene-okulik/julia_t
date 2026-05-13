def get_result(prog_result):
    index = prog_result.index(':') + 2
    return int(prog_result[index:]) + 10


print(get_result('результат операции: 42'))
print(get_result('результат операции: 514'))
print(get_result('результат работы программы: 209'))
print(get_result('результат: 2'))
