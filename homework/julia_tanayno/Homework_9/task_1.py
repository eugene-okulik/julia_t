# datetime

import datetime

date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(
    date, '%b %d, %Y - %H:%M:%S'
)
print(python_date.strftime('%B'))
print(python_date.strftime('%d.%m.%Y, %H:%M'))

# map, filter

temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
    34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
    29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

hot_temperatures = list(filter(lambda x: x > 28, temperatures))
print(hot_temperatures)
print(max(hot_temperatures))
print(min(hot_temperatures))
print(round(
    sum(hot_temperatures) / len(hot_temperatures), 1)
)
