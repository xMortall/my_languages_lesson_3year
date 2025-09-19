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

for i in range(0,2,1):
    print(" Repetição", i)

i = 0
while i < 2:
    print ("Repetição", i)
    i += 1

# Função

def repetir():
    i = 0
    while i < 2:
        print ("Repetição", i)
        i += 1

repetir()

# Função com parametros

def repetirVezes(vezes):
    i = 0
    while i < vezes:
        print ("Repetição", i)
        i += 1
    return

repetirVezes(5)

# Funcções com retorno
def somar(a, b):
    return a + b
resultado = somar(5, 3)
print ("Resultado: ", resultado)

# Livrarias

import math

raiz = math.sqrt(16)
print("raiz de quadrada de 16 é: ", raiz)
potencia = math.pow(2, 3)
print ("2 elevado a 3 é: ", potencia)

""""
Comentário de múltiplas linhas
"""

idade:int = 18
ano_de_nascimento:int = 2006

txt = f"Eu tenho {idade} anos e nasci em {ano_de_nascimento}"

