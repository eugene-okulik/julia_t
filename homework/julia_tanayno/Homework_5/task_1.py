# task_1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

# распаковка
name, last_name, city, phone, country = person

# task_2
result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'

index_1 = result_1.index(':') + 2
new_result_1 = int(result_1[index_1:]) + 10

index_2 = result_2.index(':') + 2
new_result_2 = int(result_2[index_2:]) + 10

index_3 = result_3.index(':') + 2
new_result_3 = int(result_3[index_3:]) + 10

print(new_result_1)
print(new_result_2)
print(new_result_3)

# task_3
students = ['Ivanov', 'Petrov', 'Sidorov']
students = ', '.join(students)

subjects = ['math', 'biology', 'geography']
subjects = ', '.join(subjects)

print(f'Students {students} study these subjects: {subjects}')
