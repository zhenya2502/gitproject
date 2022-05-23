# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе
my_str = "строка"
num = int()
a = ('к', 'о', 'р', 'т', 'е', 'ж')
b = list("список")
print(my_str)
print(type(my_str))
print("число")
print(type(num))
print(a)
print(type(a))
print(b)
print(type(b))

# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить
# на своем месте.
# Для заполнения списка элементов необходимо использовать
# функцию input().


# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна,
# лето, осень).
# Напишите решения через list и через dict.
mount_list = ['winter', 'spring', 'summer', 'autumn']
mount_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
mount = input()
if mount == 1 or mount == 2 or mount == 12:
    print(mount_list[0])
    print(mount_dict.get(1))
elif mount == 3 or mount == 4 or mount == 5:
    print(mount_list[1])
    print(mount_dict.get(2))
elif mount == 6 or mount == 7 or mount == 8:
    print(mount_list[2])
    print(mount_dict.get(3))
elif mount == 9 or mount == 10 or mount == 11:
    print(mount_list[3])
    print(mount_dict.get(4))
else:
    print("неправильно введен месяц")

# Пользователь вводит строку из нескольких слов, разделённых
# пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное,
# выводить только первые 10 букв в слове.
my_str = input("Enter string: ")
a = my_str.split(' ')
for i, e in enumerate(a, 1):
    if len(e) > 10:
        e = e[0:10]
    print(f"{i} " f" {e}")
