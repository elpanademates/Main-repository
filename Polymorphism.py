class Animal:
    def sounds(self):
        pass

class Cat(Animal):
    def sound(self):
        print("miau")

class Dog(Animal):
    def sound(self):
        print("woof")          

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()