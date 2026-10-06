from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/evento", methods=["POST"])
def evento():

    dados = request.json

    print("\n==============================")
    print("EVENTO RECEBIDO")
    print("==============================")

    print("Dispositivo:", dados["device"])
    print("Evento:", dados["event"])
    print("Valor:", dados["value"])

    if dados["event"] == "TEMPERATURA_ALTA":

        print("🚨 ALERTA!")
        print("Temperatura:", dados["value"], "°C")

    return jsonify({
        "status": "ok",
        "mensagem": "Evento recebido pelo servidor"
    })


app.run(host="0.0.0.0", port=5000)