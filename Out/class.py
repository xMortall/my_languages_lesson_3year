class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("jhon", 36)

print(p1.name)
print(p1.age)


class carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostraMarca(self):
        print(self.marca)

c1 = carro("BMW", "X3")
print(c1.marca)
print(c1.modelo)