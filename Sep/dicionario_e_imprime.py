"""
Programa com uma função que recebe um dicionario e imprime no ecrã no seguinte formato:
Chave: Valor
"""
def imprimir_dicionario(dicionario):
    for chave in dicionario:
        print(f"{chave} : {dicionario[chave]}")

def main():
    dicionario_exemplo:dict = {
        "Marca": "BMW",
        "Modelo": "X3",
        "Ano": "2001"
    }
    imprimir_dicionario(dicionario_exemplo)

if __name__ == "__main__":
    main()