import doctest
class Car:
    def __init__(self, brand: str, model: str, fuel_level: float = 50.0) -> None:
        """
        Создание и подготовка к работе объекта "Автомобиль"

        brand: Марка автомобиля
        model: Модель автомобиля
        fuel_level: Уровень топлива в литрах

        Raises: Если уровень топлива отрицательный

        Примеры:
        >>> car = Car("Toyota", "Camry", 40.5)
        """
        if fuel_level < 0:
            raise ValueError("Уровень топлива не может быть отрицательным")

        self.brand = brand
        self.model = model
        self.fuel_level = fuel_level

    def drive(self, distance: float) -> bool:
        """
        Проехать указанное расстояние.
        distance: Расстояние в километрах

        Returns: True если поездка успешна, False если недостаточно топлива

        Примеры:
        >>> car = Car("BMW", "X5", 60.0)
        """
        return True
        ...
    def refuel(self, liters: float) -> None:
        """
        Заправить автомобиль.
        liters: Количество литров топлива для заправки

        Raises: Если количество литров отрицательное

        Примеры:
        >>> car = Car("Volkswagen", "Golf", 20.0)
        """
        if liters < 0:
            raise ValueError("Количество литров не может быть отрицательным")

        self.fuel_level += liters
        ...

class Student:
    def __init__(self, name: str, student_id: str, average_grade: float = 0.0) -> None:
        """
        Создание и подготовка к работе объекта "Студент"

        name: Имя студента
        student_id: Номер студенческого билета
        average_grade: Средний балл (0.0-5.0)

        Raises: Если средний балл вне диапазона 0.0-5.0

        Примеры:
        >>> student = Student("Алексей Петров", "STU-2023-001", 4.5)
        """
        if not 0.0 <= average_grade <= 5.0:
            raise ValueError("Средний балл должен быть в диапазоне 0.0-5.0")

        self.name = name
        self.student_id = student_id
        self.average_grade = average_grade
        ...

    def take_exam(self, subject: str, grade: float) -> None:
        """
        Сдать экзамен по предмету.

        subject: Название предмета
        grade: Оценка за экзамен (2.0-5.0)

        Raises: Если оценка вне допустимого диапазона

        Примеры:
        >>> student = Student("Мария Иванова", "STU-2023-002", 4.2)
        """
        if not 2.0 <= grade <= 5.0:
            raise ValueError("Оценка должна быть в диапазоне 2.0-5.0")
        ...
    def calculate_scholarship(self) -> float:
        """
        Рассчитать размер стипендии.

        Returns: Размер стипендии

        Примеры:
        >>> student = Student("Дмитрий Сидоров", "STU-2023-003", 4.8)
        """
        if self.average_grade >= 4.5:
            return 2000.0
        elif self.average_grade >= 4.0:
            return 1500.0
        else:
            return 0.0
        ...

class Recipe:
    def __init__(self, name: str, cooking_time: int, difficulty: str = "Средняя") -> None:
        """
        Создание и подготовка к работе объекта "Рецепт"

        name: Название блюда
        cooking_time: Время приготовления в минутах
        difficulty: Сложность приготовления

        Raises: Если время приготовления отрицательное

        Примеры:
        >>> recipe = Recipe("Борщ", 90, "Средняя")
        """
        if cooking_time <= 0:
            raise ValueError("Время приготовления должно быть положительным")

        self.name = name
        self.cooking_time = cooking_time
        self.difficulty = difficulty

    def get_ingredients_list(self) -> list[str]:
        """
        Получить список ингредиентов.

        Returns: list[str]: Список ингредиентов

        Примеры:
        >>> recipe = Recipe("Омлет", 15, "Легкая")
        """
        return ["Яйца", "Молоко", "Соль"]
        ...

    def adjust_servings(self, servings: int) -> dict:
        """
        Скорректировать количество ингредиентов для заданного числа порций.

        servings: Количество порций

        Returns: Словарь с ингредиентами и их количеством

        Raises: Если количество порций не положительное

        Примеры:
        >>> recipe = Recipe("Салат Цезарь", 30, "Легкая")
        """
        if servings <= 0:
            raise ValueError("Количество порций должно быть положительным")
        return {"Курица": 100 * servings, "Салат": 50 * servings, "Соус": 25 * servings}
        ...

if __name__ == "__main__":
    doctest.testmod()