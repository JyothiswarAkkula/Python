class Person1:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):   #__repr__ method returns a string representation of an object that is machine-readable.
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'

    def __str__(self):   #__str__ method returns a string representation of an object that is human-readable
        return f'persons({self.first_name},{self.last_name},{self.age})'


person = Person1('John', 'Doe', 25)
person2= Person1("jyothi","ramesh",24)
# use str()
print(person)

# use repr()
print(person2)
