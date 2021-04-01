class Person:
    name = "Ivan"
    age = 10

    def set(self, name, age):
        self.name = name
        self.age = age


vlad = Person()
vlad.set("Влад", 25)
print(vlad.name + " " + str(vlad.age))

ivan = Person()
ivan.set("Иван", 56)
print(ivan.age)