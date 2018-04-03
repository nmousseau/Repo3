class Animal:
    """This is beginning of the Animal Master class"""
    def __init__(self, name):
        self.name = name
    def add_weight(self, weight):
        self.weight = weight
    def color(self, color):
        self.color = color
    
class Dog(Animal):
    """This is the beginning of the class for pet dogs"""
    def __init__(self, name, vocalization='woof'):
        super().__init__(name)
        self.vocalization = vocalization

    def speak(self):
        return "woof"
        #print("woof woof bark")    

class Cat(Animal):
    """This is the beginning of the class for pet cats"""
    def __init__(self, name, vocalization='Meow'):
        super().__init__(name)
        self.vocalization = vocalization

d = Dog('Tyroneicus')
d.color('black')
d.add_weight(10)
print(d.name)
print(d.color)
print(d.weight)
print(d.vocalization)
print('xxxxxxxxxx')
x = Dog('TyroneRoneee')
x.color('black')
x.add_weight(12)
print(x.name)
print(x.color)
print(x.weight)
print(d.vocalization)
print('xxxxxxxxxx')
c = Cat('Dark Tyrone')
c.add_weight(3)
c.color('black')
print(c.name)
print(c.weight)
print(c.color)
print(c.vocalization)
    
