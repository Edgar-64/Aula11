import network
import time

SSID = "NOME_DA_REDE"
SENHA = "SENHA_DA_REDE"

wifi = network.WLAN(network.STA_IF)

wifi.active(True)

wifi.connect(SSID, SENHA)

while not wifi.isconnected():
    print("Conectando ao Wi-Fi...")
    time.sleep(1)

print()
print("================================")
print("WI-FI CONECTADO!")
print("================================")

print("IP do ESP32:", wifi.ifconfig()[0])