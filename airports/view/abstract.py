"""
Модуль для создания абстрактных классов форм отображения
"""
from tkinter import *
from abc import ABC, abstractmethod
from tkinter import ttk
from tkinter.messagebox import showwarning
import airports.controller as c


class Form(Frame, ABC):
    """
    Абстрактный класс-предок всех форм отображения.
    """

    def __init__(self, master, geometry, title):
        """
        :param master: окно приложения
        :param geometry: размеры окна
        :param title: название окна
        """
        super().__init__(master)
        self.grid()
        self.geometry = geometry
        self.title = title

    @abstractmethod
    def create_widgets(self):
        """
        Для создание виджетов
        """
        pass


class FormInputOutput(Form):
    """
    Абстрактный класс-предок для форм отображения с выводом результатов в виде таблицы
    """

    def __init__(self, master, geometry, title):
        """
        Задает параметры окна, создает переменные для таблицы и полосы прокрутки, запускает метод создания виджетов
        :param master: окно приложения
        :param geometry: размеры окна
        :param title: название окна
        """
        super().__init__(master, geometry, title)
        self.scroll_pane = None
        self.table = None
        self.create_widgets()

    def create_table(self, heads):
        """
        Метод для создания таблицы с полосой прокрутки
        :param heads: наименование столбцов в виде списка
        """
        self.table = ttk.Treeview(self, show='headings')
        self.table['columns'] = heads
        for i in heads:
            self.table.heading(i, text=i, anchor='center')
            self.table.column(i, anchor='center')

        self.scroll_pane = ttk.Scrollbar(self, orient='vertical', command=self.table.yview)
        self.table.configure(yscrollcommand=self.scroll_pane.set)

    @abstractmethod
    def create_widgets(self):
        """
        Метод для создания виджетов
        """
        pass

    @abstractmethod
    def get_input(self):
        """
        Метод получения пользовательского ввода
        """
        pass

    @abstractmethod
    def check_input(self):
        """
        Метод проверки пользовательского ввода
        """
        pass

    def show_warning(self, msg):
        """
        Показывает сообщение с предупреждением о некорректном вводе
        :param msg: сообщение об ошибке пользовательского ввода
        """
        showwarning(title="Предупреждение", message=msg)

    def show_result_table(self):
        """
        Метод для вывода данных - результатов запроса в таблицу
        """
        self.get_input()
        if self.check_input():
            self.table.delete(*self.table.get_children())
            self.update()
            result_list = c.Controller.get_result_list()
            if len(result_list) != 0:
                if len(result_list[0]) == 5:
                    for i in result_list:
                        airport, city, country, latitude, longitude = i
                        self.table.insert('', END, values=(airport, city, country, latitude, longitude))
                else:
                    for i in result_list:
                        (airline, city_src, country_src, airport_title_src, src_airport, city_dst, country_dst,
                         airport_title_dst, dst_airport, airplane) = i
                        self.table.insert('', END,
                                          values=(city_src, country_src, airport_title_src, city_dst, country_dst,
                                                  airport_title_dst, airplane))
        else:
            self.table.delete(*self.table.get_children())
            self.update()
