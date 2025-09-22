"""
Exercicio# 1! :D
Implementa, em python, um programa que faça o seguinte:
Dada uma lista com 20 elementos, imprima no ecrã os elementos 12 -> 16
"""

# elementos:list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# print(elementos[11:17])

"""
Exercicio# 2! :D
Implementa, em python, um programa que faça o seguinte:
Dada uma lista elabora um programa que permita enserir elemntos na lista até tecla "Q" seja precionada
"""

# num = ""
# while num.lower() != "q":
#     num = input("Introduz algo: ")
#     elementos.append(num)
#     print(elementos)

"""
Exercicio# 3! :D
Implementa, em python, um programa que faça o seguinte:
Elabora um programa que apresente a sequencia de fibornacci até ao n elemento
"""

num_n:int = int(input("Quando numeros queres? "))
num1:int = 0
num2:int = 1

for num in range(num_n):
    print(num)
    num1, num2 = num2, num1 + num2
    