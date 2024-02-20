class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def get_name(self):
            return self.name
    
    def set_name(self, new_name):
         self.nombre = new_name

    def get_year(self):
         return self.edad
    
    def set_year(self, new_year):
         if new_year >= 0:
              self.year = new_year
         else:
              print("You can't be nagative years old.")

class Dog:
     def __init__(self, owner, years):
          self.owner = owner
          self.years = years

     def get_owner(self):
          return self.owner
     
     def set_owner(self, new_owner):
          self.owner = new_owner

     def get_years(self):
          return self.years
     
     def set_years(self, new_years):
        if new_years >= 0:
            self.year = new_years
        else:
            print("Your dog can't be nagative years old.")
          
persona = Person("Peter", 30)

print(persona.get_name())
persona.set_name("John")
print(persona.get_name())

print(persona.get_year())
persona.set_year(56)
print(persona.get_year())


perro = Dog("Denise", 6)

print(perro.get_owner())
perro.set_owner("Lucy")
print(perro.get_owner())

print(perro.get_years())
perro.set_years(12)
print(perro.get_years())