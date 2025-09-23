fLamb = lambda x: x * x * x
print(fLamb(5))

def fLambFunc(x):
    return x * x * x

print(fLambFunc(5))

fLamb2 = lambda: [print(i) for i in range(1, 11)]
fLamb2()

my_dict = {
    "nome": "Emerson",
    "idade": 18,
    "cidade": "Porto"
}
for dict in my_dict:
    print(dict, my_dict[dict])