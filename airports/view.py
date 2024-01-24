#import tkinter
from tkinter import *
from tkinter import ttk


class MainMenu(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Выберите действие").grid(row=1, columnspan=2, sticky=W + E, pady=10)
        Button(self, text="Аэропорты в заданных пределах", command=MainMenu.show_airports_x_y, width=40).grid(row=3,
                                                                                                              column=0,
                                                                                                              sticky=W,
                                                                                                              padx=10)
        Button(self, text="Прямые рейсы между городами", command=self.show_flights_btw_cities, width=40).grid(row=3,
                                                                                                              column=1,
                                                                                                              padx=10)
        Button(self, text="Рейсы из города", command=self.show_flights_from_city, width=20).grid(row=4, column=0,
                                                                                                 sticky=E, padx=10,
                                                                                                 pady=10)
        Button(self, text="Рейсы в город", command=self.show_flights_to_city, width=20).grid(row=4, column=1, padx=10,
                                                                                             pady=10,
                                                                                             sticky=W)

    @classmethod
    def show_airports_x_y(cls):
        airports_xy_root = Tk()
        airports_xy_root.geometry("850x375")
        airports_xy_root.title("Аэропорты в заданных пределах")
        AirportsXY(airports_xy_root)
        airports_xy_root.mainloop()

    @classmethod
    def show_flights_btw_cities(cls):
        flights_btw_cities_root = Tk()
        flights_btw_cities_root.geometry("850x375")
        flights_btw_cities_root.title("Прямые рейсы между городами")
        FlightsBtwCities(flights_btw_cities_root)
        flights_btw_cities_root.mainloop()

    def show_flights_from_city(self):
        flights_from_city_root = Tk()
        flights_from_city_root.geometry("850x375")
        flights_from_city_root.title("Рейсы из города")
        FlightsFromCity(flights_from_city_root)
        flights_from_city_root.mainloop()

    def show_flights_to_city(self):
        flights_to_city_root = Tk()
        flights_to_city_root.geometry("850x375")
        flights_to_city_root.title("Рейсы в город")
        FlightsToCity(flights_to_city_root)
        flights_to_city_root.mainloop()


class AirportsXY(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Мин. широта").grid(row=1, column=0, sticky=W, padx=10, pady=10)
        Label(self, text="Макс. широта").grid(row=2, column=0, sticky=W, padx=10, pady=10)
        Label(self, text="Мин. высота").grid(row=1, column=2, sticky=E, padx=10, pady=10)
        Label(self, text="Макс. высота").grid(row=2, column=2, sticky=E, padx=10, pady=10)
        self.lat_min = Entry(self, width=10)
        self.lat_max = Entry(self, width=10)
        self.long_min = Entry(self, width=10)
        self.long_max = Entry(self, width=10)
        self.lat_min.grid(row=1, column=1, sticky=W, padx=10, pady=10)
        self.lat_max.grid(row=2, column=1, sticky=W, padx=10, pady=10)
        self.long_min.grid(row=1, column=3, sticky=E, padx=10, pady=10)
        self.long_max.grid(row=2, column=3, sticky=E, padx=10, pady=10)
        Button(self, text="Показать", command=self.show_result_table, width=40).grid(row=3,
                                                                                     columnspan=4,
                                                                                     sticky=W + E,
                                                                                     padx=10)

        self.table = ttk.Treeview(self, show='headings')
        heads = ['Город', 'Страна', 'Широта', 'Долгота']
        self.table['columns'] = heads
        for i in heads:
            self.table.heading(i, text=i, anchor='center')
            self.table.column(i, anchor='center')

        self.scroll_pane = ttk.Scrollbar(self, orient='vertical', command=self.table.yview)
        self.table.configure(yscrollcommand=self.scroll_pane.set)
        self.scroll_pane.grid(row=4, column=5, sticky=NS)
        self.table.grid(row=4, columnspan=4, sticky=W + E, padx=10, pady=10)

    def show_result_table(self):
        self.table.delete(*self.table.get_children())
        self.update()
        # следующий код надо заменить на метод контроллера получающий фрейм данных для вывода
        self.table.insert('', END, values=('город', 'страна', 'широта', 'долгота'))
        for i in range(1, 50):
            self.table.insert('', END, values=('город' + str(i), 'страна', 'широта', 'долгота'))


class FlightsBtwCities(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text='Город отправления').grid(row=0, column=0, sticky=W, padx=10, pady=10)
        cities = ['sp', 'm']
        self.combobox_from_city = ttk.Combobox(self, values=cities)
        self.combobox_from_city.grid(row=0, column=1, sticky=NS, padx=10, pady=10)
        Label(self, text='Город прибытия').grid(row=0, column=2, sticky=W, padx=10, pady=10)
        self.combobox_to_city = ttk.Combobox(self, values=cities)
        self.combobox_to_city.grid(row=0, column=3, sticky=NS, padx=10, pady=10)
        Button(self, text="Показать", command=self.show_result_table, width=40).grid(row=3,
                                                                                     columnspan=4,
                                                                                     sticky=W + E,
                                                                                     padx=10)

        self.table = ttk.Treeview(self, show='headings')
        heads = ['Город', 'Страна', 'Широта', 'Долгота']
        self.table['columns'] = heads
        for i in heads:
            self.table.heading(i, text=i, anchor='center')
            self.table.column(i, anchor='center')

        self.scroll_pane = ttk.Scrollbar(self, orient='vertical', command=self.table.yview)
        self.table.configure(yscrollcommand=self.scroll_pane.set)
        self.scroll_pane.grid(row=4, column=5, sticky=NS)
        self.table.grid(row=4, columnspan=4, sticky=W + E, padx=10, pady=10)



class FlightsFromCity(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Мин. широта").grid(row=1, column=0, sticky=W, padx=10, pady=10)
        Label(self, text="Макс. широта").grid(row=2, column=0, sticky=W, padx=10, pady=10)


class FlightsToCity(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Мин. широта").grid(row=1, column=0, sticky=W, padx=10, pady=10)
        Label(self, text="Макс. широта").grid(row=2, column=0, sticky=W, padx=10, pady=10)


if __name__ == '__main__':
    main_menu_root = Tk()
    main_menu_root.geometry("620x140")
    main_menu_root.title("Авиасообщение")
    main_menu_form = MainMenu(main_menu_root)
    main_menu_root.mainloop()
