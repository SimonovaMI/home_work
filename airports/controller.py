from tkinter import *
import airports.view.view as v
import airports.model as m


class MainView:
    flights = None

    def show_form(self, class_form, geometry, title):
        root = Tk()
        self.flights = class_form(root, geometry, title)
        root.geometry(self.flights.geometry)
        root.title(self.flights.title)
        root.mainloop()


class Controller:
    main = MainView()
    model = m.Model

    @classmethod
    def start(cls):
        cls.model.get_result()
        cls.main.show_form(v.MainMenu, "620x140", "Авиасообщение")

    @classmethod
    def check_input_long_lat(cls):
        try:
            HelperForCheckInput.check_latitude(cls.main.flights.lat_max_value)
            HelperForCheckInput.check_latitude(cls.main.flights.lat_min_value)
        except ValueError as err:
            raise ValueError('Значение широты должно быть числом вида 89.789 в пределах от -90.0 до +90.0')
        try:
            HelperForCheckInput.check_longitude(cls.main.flights.long_max_value)
            HelperForCheckInput.check_longitude(cls.main.flights.long_min_value)
        except ValueError as err:
            raise ValueError('Значение долготы должно быть числом вида 89.789 в пределах от -180.0 до +180.0')

    @classmethod
    def show_airports_x_y(cls):
        cls.main.show_form(v.AirportsXY, "1050x375", "Аэропорты в заданных пределах")

    @classmethod
    def show_flights_btw_cities(cls):
        cls.main.show_form(v.FlightsBtwCities, "1450x375", "Рейсы между городами")

    @classmethod
    def show_flights_from_city(cls):
        cls.main.show_form(v.FlightsFromCity, "1450x375", "Рейсы из города")

    @classmethod
    def show_flights_to_city(cls):
        cls.main.show_form(v.FlightsToCity, "1450x375", "Рейсы в город")

    @classmethod
    def get_result_list(cls):
        if isinstance(cls.main.flights, v.AirportsXY):
            def filter_func(airport):
                if float(cls.main.flights.lat_min_value) <= airport[3] <= float(cls.main.flights.lat_max_value):
                    if float(cls.main.flights.long_min_value) <= airport[4] <= float(cls.main.flights.long_max_value):
                        return True
                    else:
                        return False

            return list(filter(filter_func, cls.model.result_airports))

        if isinstance(cls.main.flights, v.FlightsBtwCities):
            def filter_func(route):
                if cls.main.flights.from_city_value == route[1] and cls.main.flights.to_city_value == route[5]:
                    return True
                else:
                    return False

            return list(filter(filter_func, cls.model.result_routes))

        if isinstance(cls.main.flights, v.FlightsFromCity):
            def filter_func(route):
                if cls.main.flights.from_city_value == route[1]:
                    return True
                else:
                    return False

            return list(filter(filter_func, cls.model.result_routes))

        if isinstance(cls.main.flights, v.FlightsToCity):
            def filter_func(route):
                if cls.main.flights.to_city_value == route[5]:
                    return True
                else:
                    return False

            return list(filter(filter_func, cls.model.result_routes))

    @classmethod
    def get_cities(cls):
        return cls.model.result_cities


class HelperForCheckInput:
    @classmethod
    def check_latitude(cls, latitude):
        try:
            latitude = float(latitude)
        except ValueError:
            raise ValueError('Значение широты должно быть числом вида 89.789 в пределах от -90.0 до +90.0')
        if -90.0 <= latitude <= 90.0:
            return True
        else:
            raise ValueError('Широта должна быть в пределах от -90.0 до +90.0')

    @classmethod
    def check_longitude(cls, longitude):
        try:
            longitude = float(longitude)
        except ValueError:
            raise ValueError('Значение долготы должно быть числом вида 89.789 в пределах от -180.0 до +180.0')
        if -180.0 <= longitude <= 180.0:
            return True
        else:
            raise ValueError('Долгота должна быть в пределах от -180.0 до +180.0')


if __name__ == '__main__':
    Controller.start()
