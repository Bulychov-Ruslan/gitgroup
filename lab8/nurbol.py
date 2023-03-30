#1:
# def get_skills(resume):
#     return resume.get('skills')
# def print_resume(resume):
#     print("Name: " + resume.get('name'))
#     print("Age: " + resume.get('age'))
#     print("Education: " + resume.get('education'))
#     print("Skills: " + "".join(resume.get('skills')))
#
#
# resume = {'name':'Nurbol','age': '19','education':'Satbayev university', 'skills':'programming smart strong'}
#
# print(get_skills(resume))
# print()
#
# print_resume(resume)

# #2:
# def get_data():
#     my_list = [1, 2, 3]
#     my_tuple = (4, 5, 6)
#     my_dict = {"name": "John", "age": 25}
#     return my_list, my_tuple, my_dict
#
# result_list, result_tuple, result_dict = get_data()
#
# print(result_list)
# print(result_tuple)
# print(result_dict)

# #3:
# from functools import reduce
#
# my_list = [1, 2, 3, 4, 5]
#
# # пример использования функции map
# squared_list = list(map(lambda x: x ** 2, my_list))
# print(squared_list)
#
# # пример использования функции filter
# even_list = list(filter(lambda x: x % 2 == 0, my_list))
# print(even_list)
#
# # пример использования функции reduce
# product = reduce(lambda x, y: x * y, my_list)
# print(product)

# #4:
# def delivery_cost(street, price):
#     if "Аль-Фараби" in street or "Саина" in street or "Ташенова" in street or "Достык" in street:
#         if price < 10000:
#             return 500
#         else:
#             return 0
#     else:
#         if price < 10000:
#             return 1000
#         else:
#             return 1000
#
# print(delivery_cost('Достык 36', 100000))
#
# #5:
# def compose(f, g):
#     def h(x):
#         return f(g(x))
#     return h
#
# def f(x):
#     return x * 2
#
# def g(x):
#     return x + 1
#
# h = compose(f, g)
#
# result = h(3)
# print(result) #result:8