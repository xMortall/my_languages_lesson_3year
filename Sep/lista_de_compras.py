"""
Exerecicio: Lista de Compras
Cria uma lista chamda compras com 3 produtos a tua escolha
por exemplo Pao, Leite. Maças, Pede ao utilizador para intrudizir
um novo produto e adiciona-o a lista.
"""
import os
os.system('cls' if os.name == 'nt' else 'clear')

compras:list = ["Pão","Leite","Maçãs", "Arroz"]
adicionar_produto = input(str("Qual Produto Queres Adcionar? \n"))

compras.append(adicionar_produto)
comprimento:int = len(compras)

print(f"\nA tua lista de compras contem {comprimento} produtos: ")
virgula:chr = ", ".join(compras)
print(virgula)
