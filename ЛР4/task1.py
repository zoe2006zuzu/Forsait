class CarBrand:
    """
    Класс, представляющий марку автомобиля
    """

    def __init__(self, name: str, country: str, year: int) -> None:
        """
            name: название марки
            country: страна происхождения
            year: год основания
        """
        self._name = name
        self._country = country
        self._year = year

    def __str__(self) -> str:
        """
        Читаемое представление марки
        """
        return f"Марка: {self._name}, страна: {self._country}, основана в {self._year} г."

    def __repr__(self) -> str:
        """
        Представление для воссоздания объекта
        """
        return f"CarBrand('{self._name}', '{self._country}', {self._year})"


    def get_info(self) -> str:
        """
        Базовая информация о марке
        Название, страна, год основания
        """
        return f"{self._name} — {self._country}, основана в {self._year} году."

    def is_luxury(self) -> bool:
        """
        Относится ли марка к люксу
        true, если марка люксовая, иначе false
        """
        return False



class LandRover(CarBrand):
    """
    Дочерний класс, представляющий марку Land Rover
    """

    def __init__(self, name: str, country: str, year: int, body_type: str, offroad_class: str) -> None:
        """
            name: название марки
            country: страна происхождения
            year: год основания
            body_type: тип кузова
            offroad_class: класс внедорожной проходимости
        """
        super().__init__(name, country, year)
        self._body_type = body_type
        self._offroad_class = offroad_class

    def __str__(self) -> str:
        """
        Переопределённое строковое представление с учётом типа кузова и класса
        """
        return (f"Land Rover: {self._name}, страна: {self._country}, основана в {self._year} г., "
                f"тип: {self._body_type}, класс: {self._offroad_class}")

    def __repr__(self) -> str:
        """
        Переопределённое официальное представление
        """
        return (f"LandRover('{self._name}', '{self._country}', {self._year}, "
                f"'{self._body_type}', '{self._offroad_class}')")

    def is_luxury(self) -> bool:
        """
        причина переопределения - Land Rover - премиум
        """
        return True

if __name__ == "__main__":

    pass
