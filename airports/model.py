"""
Модуль для непосредственной работы с базой данных
"""
from mysql.connector import connect, Error
import __init__ as ini


class Model:
    """
    Класс модель для получения данных из базы данных в сыром варианте
    result_airports - аэропорты
    result_routes - рейсы
    result_cities - города
    """
    result_airports = None
    result_routes = None
    result_cities = None

    @classmethod
    def get_result(cls):
        """
        Установление соединения с базой данных. Получение массивов данных, необходимых для выполнения запросов, согласно
        требованиям к приложению. В случае проблем с соединением с базой данных возбуждается исключение.
        """
        try:
            with connect(
                    host=ini.host,
                    port=ini.port,
                    user=ini.user,
                    password=ini.password,
                    database=ini.database
            ) as connection:
                select_airports = ('SELECT airport,city,country,latitude,longitude FROM flights.airports '
                                   'ORDER BY country, city, airport;')
                select_routes = ('SELECT DISTINCT src.airline, src.city_src, src.country_src, src.airport_title_src, '
                                 'src.src_airport, dst.city as city_dst, dst.country as country_dst, '
                                 'dst.airport as airport_title_dst, dst.iata as dst_airport, src.airplane '
                                 'FROM (SELECT DISTINCT r.airline, a.city as city_src, a.country as country_src, '
                                 'a.airport as airport_title_src, r.src_airport, r.dst_airport_id as dst_airport_id, '
                                 'r.airplane as airplane FROM flights.routes AS r INNER JOIN flights.airports as a '
                                 'on r.src_airport_id = a.id) AS src INNER JOIN flights.airports as dst '
                                 'WHERE src.dst_airport_id = dst.id ORDER BY src.country_src, src.city_src,'
                                 'src.airport_title_src, dst.country, dst.city, dst.airport;')
                select_cities = 'SELECT DISTINCT city FROM flights.airports ORDER BY city;'
                with connection.cursor() as cursor:
                    cursor.execute(select_airports)
                    cls.result_airports = cursor.fetchall()
                    cursor.execute(select_routes)
                    cls.result_routes = cursor.fetchall()
                    cursor.execute(select_cities)
                    cls.result_cities = cursor.fetchall()
        except Error as e:
            raise IOError('Проблема с соединением с базой данных. Проверьте параметры в файле __ini__.py . '
                          'Повторите попытку снова.')
