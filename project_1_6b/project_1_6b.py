"""Создайте сценарий, который использует список имен файлов CSV в качестве
источника для копирования содержимого этих файлов в плоский файл. Текущая дата
и время должны быть добавлены к имени файла в качестве префикса перед
копированием. Каждая операция копирования должна быть записана в файл журнала
на локальном компьютере. Исключения для файлов, которые не были найдены,
также должны быть записаны в журнал."""

import shutil
import os
import datetime as dt


def return_files_for_copy():
    """Возвращает список абсолютных путей файлов для копирования"""
    files_list = [
        r'C:\Users\PC\Desktop\Рита Python\1_6\файлы\1.csv',
        r'C:\Users\PC\Desktop\Рита Python\1_6\файлы\2.csv',
        r'C:\Users\PC\Desktop\Рита Python\1_6\файлы\3.csv'
    ]
    return files_list


def copy_file(abspath):
    """Для копирования файла и записи в журнал информации о копировании"""
    path, filename = os.path.split(abspath)
    copy_filename = str(dt.datetime.now().strftime("%d-%m-%Y_%H-%M")) + '_' + filename
    info = f'''{filename} скопирован в {copy_filename}'''

    def write_info(info):
        """Запись в журнал о копировании"""
        with open(path + '\\' + 'журнал.txt', 'a') as info_file:
            info_file.write(info + '\n')

    try:
        shutil.copy(abspath, path + '\\' + copy_filename)
    except FileNotFoundError:
        write_info(f'''{filename}  не найден''')
    else:
        write_info(info)


def copy_files_list():
    """Для копирования всех файлов из списка"""
    for i in return_files_for_copy():
        copy_file(i)


copy_files_list()
