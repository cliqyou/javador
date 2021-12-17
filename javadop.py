import os
import time

# Вызываем в консоль возможные опции и возвращаем ее номер. Если данные не корректны, то рекурсивный вызов функции
def init_options():

    # Вызов терминала всех опций
    option = input("Введите номер опции\n1) Вывести информацию о всех модулях ядра linux\n2) Вывести информацию о загруженных модулях ядра linux\n3) Вывести модули определенной версии ядра\n4) Вывести более подробную информацию об определенном модуле\n5) Вывести время работы запущенных модулей\n6) Выход\n")

    # Проверка коректен ли ввод номера опции
    if option in ['1', '2', '3', '4', '5', '6']:
        return option

    # Иначе - рекурсивный вызов функции
    else:
        print("Некорректный ввод опции. Повторите ввод номера опциN :V")
        return init_options()

# Функция выводящая инфу о всех модулях ядра
def attributes_all_modules():
    os.system("dpkg -S *.ko | grep /lib/modules")

# Инфа о загруженных модулях ядра
def attributes_nserted_modules():
    os.system("lsmod")

# Вывод модулей определенной версии ядра
def running_modules_of_a_specific_kernel_version(specific):
    os.system("find /lib/modules/{} -name *.ko".format(specific))

# Более подробная инфа об определенном модуле
def attributes_selected_module(the_name_of_module):
    os.system("modinfo {}".format(the_name_of_module))

# Вывод времени работы запущенных модулей
def time_of_running_modules():
    os.system("uptime -p")

# Выход из программы (ехит)
def exit_the_prog():
    exit("Произведен выход из программы")

# Главная функция в которой вызываются другие функции
def main(number_of_option):
    if number_of_option == '1':
        attributes_all_modules()
    if number_of_option == '2':
        attributes_nserted_modules()
    if number_of_option == '3':
        running_modules_of_a_specific_kernel_version(input("Введите версию ядра: "))
    if number_of_option == '4':
        attributes_selected_module(input("Введите имя модуля: "))
    if number_of_option == '5':
        time_of_running_modules()
    if number_of_option == '6':
        exit_the_prog()

# Вызов главной функции и вызов метода слип для удобия
if __name__ == "__main__":
    while True:
        main(init_options())
        time.sleep(3)
