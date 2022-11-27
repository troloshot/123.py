"""
Создайте класс SpaceObject у которого будут свойство размер.
Создайте 2 класса Star и Planet которые будут наследовать SpaceObject. В классе Star добавьте свойство яркость
и метод светить в котором будет выводится на экран с какой яркостью светит звезда.
Классу Planet добавьте свойства население и прирост за год и метод который будет печатать население через переданное
ему количество лет.
"""


class SpaceObject:

    def __init__(self, size):
        self.size = size


class Star(SpaceObject):

    def __init__(self, size, brightness):
        super().__init__(size)
        self.brightness = brightness

    def shine(self):
        print(f'Яркость звезды: {self.brightness}')


class Planet(SpaceObject):

    def __init__(self, size, population, increasement):
        super().__init__(size)
        self.population = population
        self.increasement = increasement

    def population_in_years(self, years):
        print(f'Через {years} лет/год(а) населения составит {self.population + self.increasement * years} сущностей')


def check():
    star = Star(150, 234)
    star.shine()

    planet = Planet(300, 1000, 100)
    planet.population_in_years(2)


check()