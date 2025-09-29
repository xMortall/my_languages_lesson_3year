"""
Prgoma que tenha uma função que aceita uma lista de numeors inteiros e devolve a soma dosseus elementos 
Nota: A lista é de inteiros, com 5 elementos
"""

def somar_lista(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma

def main():
    lista:list = [1,2,3,4,5]
    print(somar_lista(lista))

if __name__ == "__main__":
    main()