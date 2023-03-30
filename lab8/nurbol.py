# # 1 esep

# countries = {'Казахстан': ['Иртыш', 'Есиль', 'Тобол'],
#              'Россия': ['Иртыш', 'Лена'],
#              'Украина': ['Днепр', 'Днестр', 'Дунай'],
#              'Великобритания': ['Северн', 'Темза', 'Трент'],
#              'Франция': ['Луара', 'Сена', 'Рона']}

# for country, rivers in countries.items():
#     for river in rivers:
#         print(f'{river} протекает в стране {country}')

# river_name = input('Введите название реки: ')
# for rivers in countries.values():
#     if river_name in rivers:
#         print('Река есть в словаре')
#         break
# else:
#     print('Реки нет в словаре')


# #2esep

# commentators = {}
# while True:
#     input_string = input()
#     if not input_string: # если введена пустая строка, выходим из цикла
#         break
#     name, comment = input_string.split(': ') # разбиваем входную строку на имя и комментарий
#     if name not in commentators: # если имя комментатора не встречалось ранее, добавляем его в словарь
#         commentators[name] = 1
#     else: # если имя комментатора уже встречалось ранее, увеличиваем количество его комментариев на 1
#         commentators[name] += 1
# print("Кол-во уникальных коментов: ")
# print(len(commentators)) # выводим количество уникальных комментаторов

#3esep


n = int(input()) # количество номеров телефонов
phonebook = {} # словарь для хранения номеров телефонов
for i in range(n):
    phone, name = input().split()
    phonebook[name] = phone

query = input() # запрос имени для поиска номера телефона
if query in phonebook:
    print(phonebook[query])
else:
    print("Нет в телефонной книге")


# #4esep
#
# # ввод числа сотрудников
# print("График отпусков сотрудников: ")
# n = int(input())
#
# # создание пустого словаря для отпусков
# vacation_dict = {}
#
# # заполнение словаря данными об отпусках
# for i in range(n):
#     name, day, month = input().split()
#     if month not in vacation_dict:
#         vacation_dict[month] = []
#     vacation_dict[month].append(name) #(+1 элемент)
#
# # ввод месяца запроса
# requested_month = input()
#
# # вывод фамилий сотрудников, у которых отпуск в заданном месяце
# if requested_month in vacation_dict:
#     print(" ".join(vacation_dict[requested_month]))
# else:
#     print("Никто не идет в отпуск в указанный месяц.")