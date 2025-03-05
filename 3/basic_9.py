from os import path

class Dog():
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def dark(self):
        print(f"{self.name}:Dark - I am {self.age} years old")

    def jump(self):
        print(f'{self.name}:jumpjumpjump')

my_dog = Dog('Julian', 3)
my_dog.jump()
my_dog.dark()

print(my_dog.name)
print(my_dog.age)


