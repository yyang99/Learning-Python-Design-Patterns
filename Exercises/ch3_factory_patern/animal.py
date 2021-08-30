# 简单工厂模式   允许接口创建对象，但不会暴露对象的创建逻辑
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


class ForestFactory(object):
    def make_sound(self, object_type):
        animal = eval(object_type)
        animal_obj = animal()
        return animal_obj.do_say()
        # return eval(object_type)().do_say()


if __name__ == '__main__':
    ff = ForestFactory()
    animal = input()
    ff.make_sound(animal)
