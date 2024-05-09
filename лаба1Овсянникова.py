import math
from collections import Counter
import itertools
from itertools import cycle
import json
import csv


# 1 ����� ����� ����������� ��������� ax^2 + bx + c

def quadratic_equation(a, b, c):
    if a == 0 or c == 0:
        return "��������: a � c �� ������ ���� ����� ����"
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "������������ ������ 0, ������ ������ ���"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"���� ���� ������: {root}"
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"���� ��� �����: {root1}, {root2}"


print(quadratic_equation(0, -5, 6))
print(quadratic_equation(1, -4, 4))
print(quadratic_equation(1, 5, 6))


# 2 ����� ������� �����
def circle_area(radius):
    area = math.pi * (radius ** 2)
    return f"������� ����� ����� {area}"


print(circle_area(3))


# Counter
# 1 ������� �������� �������, ������� ����������� ������ ���� ��� (��� ���/���/������ ����), � ������� � �������.
def elements_with_count(array, count):
    counter = Counter(array)
    result = []
    for element in array:
        if counter[element] == count:
            result.append(element)
    return result


array = [1, 2, 3, 4, 5, 6, 7, 2, 4, 6, 8, 2, 4, 9]
print("��������, ������� ����������� ������ ��� ����: ", elements_with_count(array, 2))


# a) ��� ������ a �� n ����� �����. �������� ���������, ������� ������ ���������� �����, ������� ���� ������
# ����������� � �������.
def most_frequent_max_number(n, a):
    counter = Counter(a)
    result = a[0]
    max_count = counter[result]
    for number, count in counter.items():
        if count > max_count or (count == max_count and number > result):
            result = number
            max_count = count
    return result


n = int(input("������� ���������� ����� � �������: "))
a = [int(i) for i in input("������� ����� ����� ������: ").split()]
print("���������� �����, ������� ���� ������ ����������� � �������: ", most_frequent_max_number(n, a))

# Itertools

# 1 ��������� ������� ������� ���� ��� �������� ���������, ������� ��������� ������������� ��� ������� �����.
# � �������� ������� ���� ������������ ������������� �����, � ������� ���� ������ ����� �, �, �, �,
# ������ ����� �̻ ���������� ����� 1 ���. ������ �� ������ ���������� ���� ����� ����������� � ������� �����
# ����� ���������� ��� ��� �� ����������� ������. ������� ��������� ������� ���� ����� ������������?

c = 0  # ������� ������� ����
a = list(itertools.product("����", repeat=6))
for x in a:
    if x.count("�") == 1:
        c += 1
print(c)

# 2 ������ ���������� �������������� ����� ���� ������������ ���� ����Δ. ������� ��������� ���� ����� ���������?

c = 0  # �������
a = list(itertools.permutations("����"))
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

# ��������� ������ JSON
# ������� ������ �������� � ����������� � ������
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

# ��������������� ������� CSV:
# 1 ���� freshman_kgs.csv - ������� ������� Weight diff, ������� ����� �������� ��������� ���� � �������� �� ������
# ������� ������ �� ������, � ������� ������������ ����������� �������� ����, ��� ������� � ���� ��������������,
# � ��� � ������ ������ ��������.

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

print('Results are in result_kgs.csv file')  # ������� ���������

# 2 ���������� ������� �������� ��������� ���� � ������� ���������
# ������� ����� �������, � ������� ���� �� ������ ���� �� ���������� ����� 180 � ������� ����� 3500.

strings = []

with open('homes.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        strings.append(row)

total_cost = 0  # ��� ��������� ��������� ���� ����� � ������� ���������
counts = 0 # ��� �������� ���������� ����� �����

for row in strings[1:]:
    if len(row) > 3 and int(row[3]) == 8:
        total_cost += (int(row[0]) * 1000 + int(row[8]))
        counts += 1

average_price = total_cost / counts  # ��������� ������� ��������� ���� � 8 ���������

new_rows = [strings[0]]

for row in strings[1:]:
    if len(row) > 8 and int(row[0]) > 180 and int(row[8]) < 3500:
        new_rows.append(row)

with open('result_homes.csv', 'w', newline='') as fin_file:
    writer = csv.writer(fin_file)
    for row in new_rows:
        writer.writerow(row)

print(f'The average price of houses with 8 rooms is {average_price}') # ������� ��������� ����
