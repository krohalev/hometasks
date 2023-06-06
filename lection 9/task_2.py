# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинковый текст, когда есть декоратор на функции func1 и когда его нет


import datetime
import time

def func_log(file_log='log.txt'):
    """
    Создание файла с названием функции и временем ее запуска
    :param file_log: уть до файла
    """
    def log(func):
        """
        :param func: функция
        """
        def wrapper(*args, **kwargs):
            """
            Открывание и заполнение файла
            """
            with open(file_log, mode="a", encoding="utf-8") as test_file:
                call_time = datetime.datetime.now().strftime("%d.%m %H:%M:%S")
                test_file.write(f"{func.__name__} вызвана {call_time}\n")

            res = func(*args, ** kwargs)
            return res

        wrapper.__doc__ = func.__doc__
        wrapper.__name__ = func.__name__
        wrapper.__wrapped__ = func
        return wrapper
    return log


@func_log()
def func1():
    """функция"""
    time.sleep(1)

help(func1)
@func_log(file_log='func2.txt')
def func2():
    """функция"""
    time.sleep(1.1)

help(func2)
def func3():
    """функция"""
    time.sleep(1.2)

help(func3)


