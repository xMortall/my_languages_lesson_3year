"""
Programa que aceita uma lista em matriz no formato:
[1 2 3]
[4 5 6]
[7 8 9]
e apresenta a lista no ecrã no mesmo formato
"""

def imprimir_matriz(matriz:list):
    for lista in matriz:
        print("[",end=" ")
        for elemento in lista:
            print(elemento,end=" ")
        print("]")

def main():
    matriz_exemplo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    imprimir_matriz(matriz_exemplo)

if __name__ == "__main__":
    main()