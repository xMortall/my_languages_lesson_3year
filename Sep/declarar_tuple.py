"""
Prgoma onde é defenido um tuplet com 4 valores e uma função que aceita como parametros um tuplet e que precorre o tuplet e imprime no ecrã o seu conteudo.
"""

def imprimir_tuplo(tuplo):
    for item in tuplo:
        print(item)

def main():
    tuplo_exemplo = (1, 2, 3, 4)
    imprimir_tuplo(tuplo_exemplo)

if __name__ == "__main__":
    main()
