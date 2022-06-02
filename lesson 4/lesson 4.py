# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.''

from sys import argv

name, n_1, n_2, n_3 = argv
print((int(n_1) * int(n_2)) + int(n_3))

# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])

# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.

# Подсказка: используйте функцию range() и генератор.

new_1 = [n for n in range(20, 240) if n % 20 == 0]
print(new_1)

# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.


# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

a = [int(i) for i in input().split()]
for i in a:
    if a.count(i) == 1:
        print(i)
# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.

# Подсказка: использовать функцию reduce().
from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, my_list))

# Реализовать два небольших скрипта:

from itertools import count
from itertools import cycle


def my_count_func(num1, num2):
    for el in count(num1):
        if el > num2:
            break
        else:
            print(el)


def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i += 1


my_count_func(num1=int(input()), num2=int(input()))
my_cycle_func(my_list=[1, 2], iteration=int(input()))
