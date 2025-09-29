f_Lamb = lambda x: x * x * x
print(f_Lamb(5))

def f_LambFunc(x):
    return x * x * x

print(f_LambFunc(5))

f_Lamb2 = lambda: [print(i) for i in range(1, 11)]
f_Lamb2()

my_dict = {
    "nome": "Emerson",
    "idade": 18,
    "cidade": "Porto"
}
for dict in my_dict:
    print(dict, my_dict[dict])