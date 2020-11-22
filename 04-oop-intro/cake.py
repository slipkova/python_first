from random import *

class Cake:
    default_color = 'white'
    default_layers = 3

    def __init__(self, l_fl, f_fl):
        self.layers = Cake.default_layers
        self.color = Cake.default_color
        self.layers_flavor = l_fl
        self.filling_flavor = f_fl
        self.decorations = []

    def __str__(self):
        return f'{self.color} cake with {self.layers} {self.layers_flavor} flavored layers and {self.filling_flavor} filling.'.capitalize()

    def __eq__(self, other):
        return self.layers_flavor == other.layers_flavor and self.filling_flavor == other.filling_flavor

    def __gt__(self, other):
        return self.layers > other.layers

    def __sub__(self, other):
        l =  self.layers - other.layers
        return max(l, -l)
        #return self.layers - other.layers if self.__gt__(other) else other.layers - self.layers

    def __add__(self, other):
        return self.layers + other.layers

    def add_decoration(self, name):
        self.decorations.append(name)

    def del_decoration(self, name):
        self.decorations.remove(name)

    @staticmethod
    def random_flavor():
        return choice(["chocolate", "vanilla", "srawberry", "blueberry", "pistachio"])

    @classmethod
    def ran_cake(cls):
        x = Cake(Cake.random_flavor(), Cake.random_flavor())
        x.layers = randrange(2, 10)
        x.color = choice(["white", "blue", "red", "orange"])
        return x

cake1 = Cake("chocolate", "strawberry")
print(cake1)
cake2 = Cake("vanilla", "chocolate")
cake2.color = "red"
cake2.layers = 5
print(cake2)
print("*****************\n")
print(cake1 == cake2)
print(cake1 > cake2)
print(cake1 - cake2)
print(cake1 + cake2)
print("\n******************\n")

cake1.add_decoration("flowers")
cake1.add_decoration("hearts")
print(cake1.decorations)
cake1.del_decoration("hearts")
print(cake1.decorations)
print("\n******************\n")

cake2.layers_flavor = Cake.random_flavor()
print(cake2)

cake3 = Cake.ran_cake()
print(cake3)