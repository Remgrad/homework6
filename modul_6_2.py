class Vehicle:  # любой транспорт
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner  # владелец транспорта. (владелец может меняться)
        self.__model = __model  # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power  # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = __color  # название цвета. (мы не можем менять цвет автомобиля своими руками)
        # self.new_color()

    # Метод    get_model - возвращает    строку: "Модель: <название модели транспорта>
    def get_model(self):
        return f'Модель: {self.__model}'

    # Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    # Метод get_color - возвращает строку: "Цвет: <цвет транспорта>
    def get_color(self):
        return f'Цвет: {self.__color}'

    # Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
    # а так же владельца в конце в формате "Владелец: <имя>"
    def print_info(self):
        print(f'{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()} \nВладелец: {self.owner}')

    # Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в
    # списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


# Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты: Атрибут __PASSENGERS_LIMIT = 5
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()
print()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
print()
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
