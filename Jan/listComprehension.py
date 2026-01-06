
nomes =  ["Ana", "Bruno", "Alice", "Carlos"]
nomes_com_a = [nome for nome in nomes if nome.startswith("A")]
print(nomes_com_a)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in numeros if num % 2 == 0]
print(pares)

celsis = [0, 10, 20, 30, 40, 50]
fahrenheits = [((9/5) * c) + 32 for c in celsis]
print(fahrenheits)

palavras = ["maçã", "banana", "cereja", "damasco"]
tamanhos = [len(palavra) for palavra in palavras]
print(tamanhos)

# ValueError

Input = input("Digite um número: ")
try:
    numero = float(Input)
    print(f"Você digitou o número: {numero}")
except ValueError:
    print("Erro: A entrada fornecida não é um número válido.")

# Key error

frutas = {
    "maçã": 3.50,
    "banana": 2.00,
    "laranjas": 4.00
}

try:
    Input = input("Digite o nome da fruta que deseja ver o preço: ")
    Input = Input.lower()
    preco = frutas[Input]
    print(f"O preço da {Input} é € {preco:.2f}")

except KeyError:
    print("Erro: A fruta solicitada não está disponível.")