# Определяем класс Animal
class Animal:
    alive = True  # Живой
    fed = False  # Накормленный

    def __init__(self, name):
        self.name = name  # Индивидуальное название


# Определяем класс Plant
class Plant:
    edible = False  # Съедобность

    def __init__(self, name):
        self.name = name  # Индивидуальное название


# Определяем класс Mammal, наследующий от Animal
class Mammal(Animal):
    def eat(self, food):
        if food.edible:  # Проверка на съедобность
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


# Определяем класс Predator, наследующий от Animal
class Predator(Animal):
    def eat(self, food):
        if food.edible:  # Проверка на съедобность
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


# Определяем класс Flower, наследующий от Plant
class Flower(Plant):
    pass  # Цветы по умолчанию несъедобные


# Определяем класс Fruit, наследующий от Plant
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем edible как True


# Создаем объекты классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка атрибутов
print(a1.name)  # Вывод: Волк с Уолл-Стрит
print(p1.name)  # Вывод: Цветик семицветик

print(a1.alive)  # Вывод: True
print(a2.fed)  # Вывод: False

# Хищник пытается съесть цветок (несъедобный)
a1.eat(p1)

# Млекопитающее ест фрукт (съедобный)
a2.eat(p2)

print(a1.alive)  # Вывод: False (погиб)
print(a2.fed)  # Вывод: True (насытился)