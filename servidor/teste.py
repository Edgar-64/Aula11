import requests

url = "http://127.0.0.1:5000/evento"

dados = {
    "device": "TESTE_PC",
    "event": "TEMPERATURA_ALTA",
    "value": 35.7
}

resposta = requests.post(url, json=dados)

print("Resposta do servidor:")
print(resposta.text)