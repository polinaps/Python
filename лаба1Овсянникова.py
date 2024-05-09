import math
from collections import Counter
import itertools
from itertools import cycle
import json
import csv


# 1 Найти корни квадратного уравнения ax^2 + bx + c

def quadratic_equation(a, b, c):
    if a == 0 or c == 0:
        return "Внимание: a и c не должны быть равны нулю"
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "Дискриминант меньше 0, значит корней нет"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"Есть один корень: {root}"
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Есть два корня: {root1}, {root2}"


print(quadratic_equation(0, -5, 6))
print(quadratic_equation(1, -4, 4))
print(quadratic_equation(1, 5, 6))


# 2 Найти площадь круга
def circle_area(radius):
    area = math.pi * (radius ** 2)
    return f"Площадь круга равна {area}"


print(circle_area(3))


# Counter
# 1 Вывести элементы массива, которые встречаются только один раз (или два/три/четыре раза), в порядке в массиве.
def elements_with_count(array, count):
    counter = Counter(array)
    result = []
    for element in array:
        if counter[element] == count:
            result.append(element)
    return result


array = [1, 2, 3, 4, 5, 6, 7, 2, 4, 6, 8, 2, 4, 9]
print("Элементы, которые встречаются только два раза: ", elements_with_count(array, 2))


# a) Дан массив a из n целых чисел. Напишите программу, которая найдет наибольшее число, которое чаще других
# встречается в массиве.
def most_frequent_max_number(n, a):
    counter = Counter(a)
    result = a[0]
    max_count = counter[result]
    for number, count in counter.items():
        if count > max_count or (count == max_count and number > result):
            result = number
            max_count = count
    return result


n = int(input("Введите количество чисел в массиве: "))
a = [int(i) for i in input("Введите числа через пробел: ").split()]
print("Наибольшее число, которое чаще других встречается в массиве: ", most_frequent_max_number(n, a))

# Itertools

# 1 составить таблицу кодовых слов для передачи сообщений, каждому сообщению соответствует своё кодовое слово.
# В качестве кодовых слов используются пятибуквенные слова, в которых есть только буквы А, Т, О, М,
# причём буква «М» появляется ровно 1 раз. Каждая из других допустимых букв может встречаться в кодовом слове
# любое количество раз или не встречаться совсем. Сколько различных кодовых слов можно использовать?

c = 0  # счетчик кодовых слов
a = list(itertools.product("атом", repeat=6))
for x in a:
    if x.count("м") == 1:
        c += 1
print(c)

# 2 Ученик составляет шестибуквенные слова путём перестановки букв “НЕБО”. Сколько различных слов можно составить?

c = 0  # счетчик
a = list(itertools.permutations("НЕБО"))
print(len(set(a)))


def infinite(lst, iterations):
    result = ''
    iter_lst = cycle(lst)
    if lst:
        for symbol in range(iterations):
            result += str(next(iter_lst))
    return result


print(infinite([2, 5, 8], 7))
print(infinite([], 1000))
print(infinite([7], 4))

# Обработка данных JSON
# Создаем список словарей с информацией о книгах
books = [{'title': 'Biology', 'author': 'One', 'pages': 550},
         {'title': 'English', 'author': 'Two', 'pages': 450},
         {'title': 'Python', 'author': 'Three', 'pages': 600},
         {'title': 'Linguistics', 'author': 'Four', 'pages': 350},
         {'title': 'Literature', 'author': 'Five', 'pages': 700}]

with open('books.json', 'w') as file:
    json.dump(books, file)
with open('books.json', 'r') as file:
    books = json.load(file)

long_books = []

for book in books:
    if book['pages'] > 500:
        long_books.append(book)
for book in long_books:
    print(book['title'])

# Манипулирование данными CSV:
# 1 Файл freshman_kgs.csv - создать столбец Weight diff, который будет отражать изменение веса с сентября по апрель
# Вывести только те строки, в которых представлены респонденты мужского пола, чья разница в весе неотрицательна,
# а ИМТ в апреле больше двадцати.

with open('freshman_kgs.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    for i in csv_reader:
        sex = i[0]
        weight_diff = int(i[1]) - int(i[2])
        bmi = float(i[4])

with open('result_kgs.csv', mode='w', newline='') as out_file:
    csv_writer = csv.writer(out_file)
    csv_writer.writerow(header + ['Wight diff'])

    if sex == 'M' and weight_diff >= 0 and bmi > 20.0:
        weight_diff = str(weight_diff)
        csv_writer.writerow(i + [
            weight_diff])

print('Results are in result_kgs.csv file')  # Выводим сообщение

# 2 рассчитать среднюю итоговую стоимость дома с восемью комнатами
# создать новый столбец, в котором были бы только дома со стоимостью более 180 и налогом менее 3500.

strings = []

with open('homes.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        strings.append(row)

total_cost = 0  # для суммарной стоимости всех домов с восемью комнатами
counts = 0 # для подсчета количества таких домов

for row in strings[1:]:
    if len(row) > 3 and int(row[3]) == 8:
        total_cost += (int(row[0]) * 1000 + int(row[8]))
        counts += 1

average_price = total_cost / counts  # Вычисляем среднюю стоимость дома с 8 комнатами

new_rows = [strings[0]]

for row in strings[1:]:
    if len(row) > 8 and int(row[0]) > 180 and int(row[8]) < 3500:
        new_rows.append(row)

with open('result_homes.csv', 'w', newline='') as fin_file:
    writer = csv.writer(fin_file)
    for row in new_rows:
        writer.writerow(row)

print(f'The average price of houses with 8 rooms is {average_price}') # средняя стоимость дома
