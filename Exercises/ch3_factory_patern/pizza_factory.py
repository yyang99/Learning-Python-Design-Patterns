# 抽象工厂模式  抽象工厂是一个能够创建一系列相关对象而无需指定/公开其具体类的接口。
# 			   该模式能够提供其他工厂的对象, 在其内部创建其他对象。

from abc import ABCMeta, abstractmethod

class PizzaFactory(metaclass=ABCMeta):
	@abstractmethod
	def createVegPizza(self):
		pass

	@abstractmethod
	def createNonVegPizza(self):
		pass

class IndianPizzaFactory(PizzaFactory):
	def createVegPizza(self):
		return DeluxVeggiePizza()

	def createNonVegPizza(self):
		return ChickenPizza()

class USPizzaFactory(PizzaFactory):
	def createVegPizza(self):
		return MexicanVegPizza()

	def createNonVegPizza(self):
		return HamPizza()


class VegPizza(metaclass=ABCMeta):
	@abstractmethod
	def prepare(self, VegPizza):
		pass

class NonVegPizza(metaclass=ABCMeta):
	@abstractmethod
	def serve(self, VegPizza):
		pass

class DeluxVeggiePizza(VegPizza):
	def prepare(self):
		print("Prepare ", type(self).__name__)

class ChickenPizza(NonVegPizza):
	def serve(self, VegPizza):
		print(type(self).__name__, " is served with Chicken on ", type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
	def prepare(self):
		print("Prepare ", type(self).__name__)

class HamPizza(NonVegPizza):
	def serve(self, VegPizza):
		print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)



class PizzaStore:
	def __init__(self):
		pass

	def makePizzas(self):
		for factory in [IndianPizzaFactory(), USPizzaFactory()]:
			self.factory = factory
			self.NonVegPizza = self.factory.createNonVegPizza()
			self.VegPizza = self.factory.createVegPizza()
			self.VegPizza.prepare()
			self.NonVegPizza.serve(self.VegPizza)

pizza = PizzaStore()
pizza.makePizzas()
