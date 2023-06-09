

## Фабрика (Factory)


class Dog:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())


## Абстрактная фабрика (Abstract Factory)



class Dog:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Woof!"

class DogFactory:
    def get_pet(self):
        return Dog("Hope")
    
    def get_food(self):
        return "Dog Food"

class Cat:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Meow!"

class CatFactory:
    def get_pet(self):
        return Cat("Peace")
    
    def get_food(self):
        return "Cat Food"

class PetStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory
    
    def show_pet(self):
        pet = self._pet_factory.get_pet()
        print("This is a lovely", pet.name)
        print("It says", pet.speak())
        print("It eats", self._pet_factory.get_food())

factory = DogFactory()

shop = PetStore(factory)

shop.show_pet()


## Строитель (Builder)


class Director:
    def __init__(self, builder):
        self._builder = builder
    
    def construct_building(self):
        self._builder.new_building()
        self._builder.build_floor()
        self._builder.build_size()

    def get_building(self):
        return self._builder.building

class Builder:
    def __init__(self):
        self.building = None
    
    def new_building(self):
        self.building = Building()

class Building:
    def __init__(self):
        self.floor = None
        self.size = None
    
    def __repr__(self):
        return f"Floor: {self.floor} | Size: {self.size}"

class House(Builder):
    def build_floor(self):
        self.building.floor = "One"
    
    def build_size(self):
        self.building.size = "Big"

class Flat(Builder):
    def build_floor(self):
        self.building.floor = "Many"
    
    def build_size(self):
        self.building.size = "Small"

house_builder = House()
director = Director(house_builder)
director.construct_building()
house = director.get_building()

flat_builder = Flat()
director = Director(flat_builder)
director.construct_building()
flat = director.get_building()

print(house)
print(flat)



