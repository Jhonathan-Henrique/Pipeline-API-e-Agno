import requests
import time
from datetime import datetime
from tinydb import TinyDB


def extrair():
    '''Aqui criei a função de extrair, na URL guardo o valor da API
    na variavel responde eu uso o metodo requests para pegar com get() os valores da api
    E retorno eles no formato Json'''
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()

def transformar(dados_json): #Aqui criei uma função e passei dados_jason como parametro, só isso!
    valor = dados_json['data']['amount']
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    dados_tratados = {
            "valor": valor,
            "criptomoeda": criptomoeda,
            "moeda": moeda,
            "timestamp": datetime.now().isoformat()
    }
    return dados_tratados

def load(dados_tratados):
    db = TinyDB('db.json')
    db.insert(dados_tratados)
    print('Os dados foram salvos com sucesso!')

if __name__ == "__main__":
    while True:
        dados_json = extrair()
        dados_tratados = transformar(dados_json)
        load(dados_tratados)
        time.sleep(5)


