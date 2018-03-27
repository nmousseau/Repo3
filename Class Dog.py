class Dog:
    """ This is the beginning of a class for the humble house dog """

    def __init__(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

    def add_noise(self, noise):
        self.noise = noise


d = Dog('Tyroneicus')

x = Dog('DarkTyrone')

x.add_weight(12)
d.add_noise("bark")
x.add_noise("bark")

print(d.name)

print(x.name)
print(x.weight)
print(d.noise)
print(x.noise)

    
