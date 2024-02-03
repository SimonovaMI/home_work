from tkinter import *
from tkinter import ttk
import airports.view.abstract as abstract
import airports.controller as c


class MainMenu(abstract.Form):

    def __init__(self, master, geometry, title):
        super().__init__(master, geometry, title)
        self.create_widgets()

    def create_widgets(self):
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

    def get_input(self):
        self.long_max_value = self.long_max.get()
        self.long_min_value = self.long_min.get()
        self.lat_max_value = self.lat_max.get()
        self.lat_min_value = self.lat_min.get()

    def create_widgets(self):
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
        try:
            c.Controller.check_input_long_lat()
            return True
        except ValueError as err:
            self.show_warning(err)
            return False


class FlightsBtwCities(abstract.FormInputOutput):
    def get_input(self):
        self.from_city_value = self.combobox_from_city.get()
        self.to_city_value = self.combobox_to_city.get()

    def create_widgets(self):
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
        return True


class FlightsFromCity(abstract.FormInputOutput):
    def get_input(self):
        self.from_city_value = self.combobox_from_city.get()

    def create_widgets(self):
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
        return True


class FlightsToCity(abstract.FormInputOutput):

    def get_input(self):
        self.to_city_value = self.combobox_to_city.get()

    def create_widgets(self):
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
        return True
