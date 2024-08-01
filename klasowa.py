class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls("Kamil").population 
        #z konstruktorem
        
        #return cls.population 
        #bez uruchomienia konstruktora

# Tworzenie obiektów klasy Person
p1 = Person("Alice")
p2 = Person("Bob")

# Wywołanie metody klasowej
print(Person.get_population())
print(Person.population)
