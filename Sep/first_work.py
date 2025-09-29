"""
first work in python
"""

x:int = 5
y:int = 5
z:int = 5

x, y, z = 1, 2, 3

marcas:list = ["Nile", "Adidas", "Puma"]

for i in marcas:
    print(i)

def HelloWorld(nome):
    print(nome)

x = "awesome"

def my_func():
    global x
    x = "cool"
    print("Python is " + x)

my_func()

HelloWorld("print")

print(type(x))
print(x)