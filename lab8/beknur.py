#1esep
# countries = {'Казахстан': ['Урал', 'Сыр-Дария', 'Или'],
#              'Россия': ['Обь', 'Волга', 'Дон'],
#              'Германия': ['Райн', 'Эльба', 'Везер'],
#              'Бразилия': ['Амазонка', 'Парана'],
#              'Китай': ['Меконг', 'Ло', 'Хонгха']}
# for country, rivers in countries.items():
#     for river in rivers:
#         print(f'{river} протекает в стране {country}')
# river_name = input('Введите реку: ')
# for rivers in countries.values():
#     if river_name in rivers:
#         print('Есть')
#         break
# else:
#     print('Нет')
# country_name = input("Введите страну: ")
# river_name = input("Введите реку: ")
# if country_name in countries:
#     countries[country_name].append(river_name)
# else:
#     countries[country_name] = [river_name]
# print(countries)

#2esep
# commentators = {}
# while True:
#     comments = input()
#     if not comments:
#         break
#     name, comment = comments.split(': ')
#     if name not in commentators:
#         commentators[name] = 1
#     else:
#         commentators[name] += 1
# print(len(commentators))

#3esep
# n = int(input())
# phonebook = {}
# for i in range(n):
#     name, phone = input().split()
#     phonebook[name] = phone
# find = input()
# if find in phonebook:
#     print(phonebook[find])
# else:
#     print("Нет в телефонной книге")

#4esep
# n = int(input())
# vacation_dict = {}
# for i in range(n):
#     name, day, month = input().split()
#     if month not in vacation_dict:
#         vacation_dict[month] = []
#     vacation_dict[month].append(name)
# requested_month = input()
# if requested_month in vacation_dict:
#     print(" ".join(vacation_dict[requested_month]))
# else:
#     print(" ")


# n = int(input('N = '))
# d = {
#     'Kazakhstan' : 'Esil',
#     'France' : 'Qwe',
#     'Russia' : 'qwrsf',
#     'Germany' : 'fsdgs',
#     'USA' : 'dsfs',
#     'China' : 'sdgdfg',
#     'Japan' : 'dsfsdg'
# }
# print(d)