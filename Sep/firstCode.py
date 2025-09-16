idade:int = int(input("Qual a tua idade? "))
estudante:bool = True


#Operadores artméticos
print(idade + 5)
print(idade * 5)
print(idade - 5)
print(idade / 5)

# Instrução Condicional
if idade < 18:
    print ("Menor de idade")
elif idade == 18:
    print ("Acabaste de fazer 18 anos")
else:
    print("Maior de idade")

# Operadores de comparação
print(idade > 18)
print(idade == 18)
print(idade != 18)
print(idade <= 18)
print(idade >= 18)
print(idade < 18)
print(idade >= 18 and estudante)
print(idade >= 18 or estudante)
print(not estudante)


# Laços de repetição

for i in range(1, 6):
    print(" Repetição", i)