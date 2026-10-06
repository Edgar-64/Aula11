import network
import time
import urequests
import dht
from machine import Pin

SSID = "POCO C75"
SENHA = "91i3t2behf8"

URL = "http://10.237.103.52:5000/evento"


# =========================
# RESET DO WI-FI
# =========================

wifi = network.WLAN(network.STA_IF)

wifi.active(False)
time.sleep(1)

wifi.active(True)
time.sleep(1)

wifi.connect(SSID, SENHA)

while not wifi.isconnected():

    print("Conectando ao Wi-Fi...")
    time.sleep(1)

print("Wi-Fi conectado!")
print("IP do ESP32:", wifi.ifconfig()[0])


# =========================
# DHT11 - GPIO 4
# =========================

sensor = dht.DHT11(Pin(4))

try:

    time.sleep(2)

    sensor.measure()

    temperatura = sensor.temperature()
    umidade = sensor.humidity()

    print("DHT11 funcionando!")
    print("Temperatura:", temperatura)
    print("Umidade:", umidade)

except Exception as erro:

    print("DHT11 não respondeu:", erro)
    print("Usando valores simulados...")

    temperatura = 40
    umidade = 60

    print("Temperatura simulada:", temperatura)
    print("Umidade simulada:", umidade)


# =========================
# EVENTO
# =========================

if temperatura > 30:

    evento = "TEMPERATURA_ALTA"

else:

    evento = "TEMPERATURA_NORMAL"


dados = {
    "device": "ESP32_01",
    "event": evento,
    "value": temperatura
}

print("Evento:", evento)


# =========================
# ENVIAR PARA O SERVIDOR
# =========================

try:

    print("Enviando evento...")

    resposta = urequests.post(
        URL,
        json=dados
    )

    print("Resposta do servidor:")
    print(resposta.text)

    resposta.close()

except Exception as erro:

    print("Erro ao enviar:")
    print(erro)