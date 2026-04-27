# task_1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

# распаковка
name, last_name, city, phone, country = person

# task_2 (вроде решила задачу с помощью среза без index,
# не сообразила, как тут применить index)
result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'

new_result_1 = int(result_1[20:]) + 10
new_result_2 = int(result_2[20:]) + 10
new_result_3 = int(result_3[28:]) + 10

print(new_result_1)
print(new_result_2)
print(new_result_3)

# task_3
students = ['Ivanov', 'Petrov', 'Sidorov']
students = ', '.join(students)

subjects = ['math', 'biology', 'geography']
subjects = ', '.join(subjects)

print(f'Students {students} study these subjects: {subjects}')
