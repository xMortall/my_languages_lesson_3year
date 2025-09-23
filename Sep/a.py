"""
Consulte uma api publica e imprima o resultado no ecrã
"""
import requests

def consultar_api():
    pokemon = str(input("Qual o nome do pokemon que queres consultar? "))
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    resposta = requests.get(url)

    if resposta.status_code == 200:  # Sucesso
        dados = resposta.json()  # Converte para dicionário Python
        print("Nome:", dados["name"])
        print("Altura:", dados["height"], "Cm")
        print("Peso:", dados["weight"] / 10, "Kg")
        print("Tipo(s):", ", ".join([tipo["type"]["name"] for tipo in dados["types"]]))
    else:
        print("Erro ao consultar API:", resposta.status_code)

consultar_api()
