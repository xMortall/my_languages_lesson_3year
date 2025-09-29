import requests

def obter_sismos():

    idArea = str(input("Qual a área que queres consultar? (Acores ou Madeira) "))
    if idArea.lower() == "acores":
        idArea = 3
    elif idArea.lower() == "madeira":
        idArea = 7

    url = f"https://api.ipma.pt/open-data/observation/seismic/{idArea}.json"
    resp = requests.get(url)
    if resp.status_code == 200:
        dados = resp.json()
        for sismo in dados["data"]:
            print(f"Data: {sismo["dataUpdate"]}, Magnitude: {sismo["magnitud"]}, Local: {sismo["local"]}")
    else:
        print("Erro ao consultar a API:", resp.status_code)

def main():
    obter_sismos()

if __name__ == "__main__":
    main()
