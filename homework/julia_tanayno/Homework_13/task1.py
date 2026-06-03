import os
import datetime

# в какой папке находится текущий файл
base_path = os.path.dirname(__file__)
# поднялись на два уровня выше (до homework)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

# сделала чтение файла построчно
with open(data_file_path) as data_file:
    now = datetime.datetime.now()
    for data_line in data_file:
        # вычленила дату
        start = data_line.index('. ') + 2
        end = data_line.index(' -')
        date_str = data_line[start:end]
        # вычленила номер
        number = int(data_line[0:data_line.index('.')])
        # преобразовала дату-строку в формат даты
        python_date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
        if number == 1:
            print(python_date + datetime.timedelta(weeks=1))
        elif number == 2:
            print(python_date.weekday())
        elif number == 3:
            how_many_days_ago = now - python_date
            print(how_many_days_ago.days)
