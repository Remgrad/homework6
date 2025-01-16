# Animal - класс описывающий животных.
# Класс обладает следующими атрибутами:
# live = True
# sound = None - звук (изначально отсутствует)
# _DEGREE_OF_DANGER = 0 - степень опасности существа
import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    # Объект этого класса обладает следующими атрибутами:
    # _cords = [0, 0, 0] - координаты в пространстве.
    # speed = ... - скорость передвижения существа (определяется при создании объекта)
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    # И методами:
    #
    # move(self, dx, dy, dz), который должен менять соответствующие кооординаты в _cords на dx, dy и dz в том же порядке,
    # где множетелем будет являтся speed. Если при попытке изменения координаты z в _cords значение будет меньше 0,
    # то выводить сообщение "It's too deep, i can't dive :(" , при этом изменения не вносяться.
    # get_cords(self), который выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
    # attack(self), который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и
    # "Be careful, i'm attacking you 0_0" , если равно или больше.
    # speak(self), который выводит строку со звуком sound.
    def move(self, dx, dy, dz):
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [new_x, new_y, new_z]

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    # Sorry, i'm peaceful :)", если степень опасности меньше 5
    # Be careful, i'm attacking you 0_0" , если равно или больше


# Bird - класс описывающий птиц. Наследуется от Animal.
# Должен обладать атрибутом:
# beak = True - наличие клюва
# И методом:
# lay_eggs(self), который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
class Bird(Animal):
    beak = True

    def lay_eggs(self):
        num_of_eggs = random.randint(1, 4)
        print(f"Here are(is) {num_of_eggs} eggs for you")


# AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal.
# В этом классе атрибут _DEGREE_OF_DANGER = 3.
#  Должен обладать методом:
# dive_in(self, dz) - где dz изменение координаты z в _cords. Этот метод должен всегда уменьшать координату z в _coords.
# Чтобы сделать dz положительным, берите его значение по модулю (функция abs). Скорость движения при нырянии должна
# уменьшаться в 2 раза, в отличии от обычного движения. (speed / 2)
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        new_z = self._cords[2] - abs(dz) * .5 * self.speed
        self._cords[2] = max(new_z, 0)


# PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal.
# В этом классе атрибут _DEGREE_OF_DANGER = 8.
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


# Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
# Порядок наследования определите сами, опираясь на ниже приведённые примеры выполнения кода.
# Объект этого класса должен обладать одним дополнительным атрибутом:
# sound = "Click-click-click" - звук, который издаёт утконос
class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)

    def speak(self):
        print(self.sound)


db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()
db.move(1, 2, 3)

db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
