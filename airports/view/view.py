"""
Модуль для создания классов форм отображения
"""
from tkinter import *
from tkinter import ttk
import airports.view.abstract as abstract
import airports.controller as c


class MainMenu(abstract.Form):
    """
    Класс создания формы главного меню
    """

    def __init__(self, master, geometry, title):
        """
        Установка параметров окна, вывод метода создания виджетов
        :param master: окно приложения
        :param geometry: размеры окна
        :param title: название окна
        """
        super().__init__(master, geometry, title)
        self.create_widgets()

    def create_widgets(self):
        """
        Для создания виджетов в главной формы
        """
        Label(self, text="Выберите действие").grid(row=1, columnspan=2, sticky=W + E, pady=10)
        (Button(self, text="Аэропорты в заданных пределах", command=c.Controller.show_airports_x_y, width=40).grid(
            row=3,
            column=0,
            sticky=W,
            padx=10))
        Button(self, text="Прямые рейсы между городами", command=c.Controller.show_flights_btw_cities, width=40).grid(
            row=3,
            column=1,
            padx=10)
        Button(self, text="Рейсы из города", command=c.Controller.show_flights_from_city, width=20).grid(row=4,
                                                                                                         column=0,
                                                                                                         sticky=E,
                                                                                                         padx=10,
                                                                                                         pady=10)
        Button(self, text="Рейсы в город", command=c.Controller.show_flights_to_city, width=20).grid(row=4, column=1,
                                                                                                     padx=10,
                                                                                                     pady=10,
                                                                                                     sticky=W)


class AirportsXY(abstract.FormInputOutput):
    """
    Класс создания формы для поиска аэропортов, находищихся в пределах широт и долгот, указанных пользователем
    """

    def create_widgets(self):
        """
        Создает виджеты
        """
        Label(self, text="Мин. широта").grid(row=1, column=0, sticky=W, padx=10, pady=10)
        Label(self, text="Макс. широта").grid(row=2, column=0, sticky=W, padx=10, pady=10)
        Label(self, text="Мин. долгота").grid(row=1, column=2, sticky=E, padx=10, pady=10)
        Label(self, text="Макс. долгота").grid(row=2, column=2, sticky=E, padx=10, pady=10)
        self.lat_min = Entry(self, width=10)
        self.lat_max = Entry(self, width=10)
        self.long_min = Entry(self, width=10)
        self.long_max = Entry(self, width=10)
        self.lat_min.grid(row=1, column=1, sticky=W, padx=10, pady=10)
        self.lat_max.grid(row=2, column=1, sticky=W, padx=10, pady=10)
        self.long_min.grid(row=1, column=3, sticky=E, padx=10, pady=10)
        self.long_max.grid(row=2, column=3, sticky=E, padx=10, pady=10)
        Button(self, text="Показать", command=self.show_result_table, width=40).grid(row=3,
                                                                                     columnspan=8,
                                                                                     sticky=W + E,
                                                                                     padx=10)
        self.create_table(['Аэропорт', 'Город', 'Страна', 'Широта', 'Долгота'])
        self.scroll_pane.grid(row=4, column=5, sticky=NS)
        self.table.grid(row=4, columnspan=4, sticky=W + E, padx=10, pady=10)

    def check_input(self):
        """
        Проверяет введенные данные до запуска процесса поиска
        """
        try:
            c.Controller.check_input_long_lat()
            return True
        except ValueError as err:
            self.show_warning(err)
            return False

    def get_input(self):
        """
        Получает значения минимальных и максимальных широт и долгот, введенных пользователем
        """
        self.long_max_value = self.long_max.get()
        self.long_min_value = self.long_min.get()
        self.lat_max_value = self.lat_max.get()
        self.lat_min_value = self.lat_min.get()


class FlightsBtwCities(abstract.FormInputOutput):
    """
    Класс создания формы поиска прямых рейсов между двумя городами, выбранными пользователем
    """

    def create_widgets(self):
        """
        Создает виджеты
        """
        Label(self, text='Город отправления').grid(row=0, column=0, sticky=W, padx=10, pady=10)
        self.combobox_from_city = ttk.Combobox(self, values=c.Controller.get_cities())
        self.combobox_from_city.grid(row=0, column=1, sticky=NS, padx=10, pady=10)
        Label(self, text='Город прибытия').grid(row=0, column=2, sticky=W, padx=10, pady=10)
        self.combobox_to_city = ttk.Combobox(self, values=c.Controller.get_cities())
        self.combobox_to_city.grid(row=0, column=3, sticky=NS, padx=10, pady=10)
        Button(self, text="Показать", command=self.show_result_table, width=40).grid(row=3,
                                                                                     columnspan=8,
                                                                                     sticky=W + E,
                                                                                     padx=10)
        self.create_table((['Город отправления', 'Страна отправления', 'Аэропорт отправления',
                            'Город прибытия', 'Страна прибытия', 'Аэропорт прибытия', 'Самолет']))
        self.scroll_pane.grid(row=4, column=5, sticky=NS)
        self.table.grid(row=4, columnspan=4, sticky=W + E, padx=10, pady=10)

    def check_input(self):
        """
        Возможная проверка введенных данных пользователем
        :return: True
        """
        return True

    def get_input(self):
        """
        Получает город отправления и прибытия для поиска
        """
        self.from_city_value = self.combobox_from_city.get()
        self.to_city_value = self.combobox_to_city.get()


class FlightsFromCity(abstract.FormInputOutput):
    """
    Класс создания формы поиска рейсов из города, выбранного пользователем
    """

    def create_widgets(self):
        """
        Создает виджеты
        """
        Label(self, text='Город отправления').grid(row=0, column=0, sticky=W, padx=10, pady=10)
        self.combobox_from_city = ttk.Combobox(self, values=c.Controller.get_cities())
        self.combobox_from_city.grid(row=0, column=1, sticky=NS, padx=10, pady=10)
        Button(self, text="Показать", command=self.show_result_table, width=40).grid(row=3,
                                                                                     columnspan=2,
                                                                                     sticky=W + E,
                                                                                     padx=10)
        self.create_table(['Город отправления', 'Страна отправления', 'Аэропорт отправления',
                           'Город прибытия', 'Страна прибытия', 'Аэропорт прибытия', 'Самолет'])
        self.scroll_pane.grid(row=4, column=3, sticky=NS)
        self.table.grid(row=4, columnspan=2, sticky=W + E, padx=10, pady=10)

    def check_input(self):
        """
        Возможная проверка введенных данных пользователем
        :return: True
        """
        return True

    def get_input(self):
        """
        Получает город отправления для поиска
        """
        self.from_city_value = self.combobox_from_city.get()


class FlightsToCity(abstract.FormInputOutput):
    """
    Класс создания формы поиска рейсов в город, выбранный пользователем
    """

    def create_widgets(self):
        """
        Создает виджеты
        """
        Label(self, text='Город прибытия').grid(row=0, column=0, sticky=W, padx=10, pady=10)
        self.combobox_to_city = ttk.Combobox(self, values=c.Controller.get_cities())
        self.combobox_to_city.grid(row=0, column=1, sticky=NS, padx=10, pady=10)
        Button(self, text="Показать", command=self.show_result_table, width=40).grid(row=3,
                                                                                     columnspan=2,
                                                                                     sticky=W + E,
                                                                                     padx=10)

        self.create_table(['Город отправления', 'Страна отправления', 'Аэропорт отправления',
                           'Город прибытия', 'Страна прибытия', 'Аэропорт прибытия', 'Самолет'])
        self.scroll_pane.grid(row=4, column=3, sticky=NS)
        self.table.grid(row=4, columnspan=2, sticky=W + E, padx=10, pady=10)

    def check_input(self):
        """
        Возможная проверка введенных данных пользователем
        :return: True
        """
        return True

    def get_input(self):
        """
        Получает город прибытия для поиска
        """
        self.to_city_value = self.combobox_to_city.get()
