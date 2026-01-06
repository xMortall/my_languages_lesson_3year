lista =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = list(map(lambda x: x ** 2, lista))

pares = list(filter(lambda x: x % 2 == 0, lista))

print(quadrados)
print(pares)

# filtrar palvreas curtas: dada uma lista de palvras ["sol", "computador", "lua", "python", "mar"]
# usa filter() para criar uma lista que contenha apenas palvras com mais 3 letras.

palavras = ["sol", "computador", "lua", "python", "mar"]
palavras_longas = list(filter(lambda palavra: len(palavra) > 3, palavras))
print(palavras_longas)

# Conversão de preços: TEns uma lista de preços em euros [10, 50, 100]
# Usa map() para aplicar um desconto de 10% a cada preço
# (multiplicar por 0.9)

precos_euros = [10, 50, 100]
precos_com_desconto = list(map(lambda preco: preco * 0.9, precos_euros))
print(precos_com_desconto)