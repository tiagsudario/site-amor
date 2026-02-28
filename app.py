from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    fotos = [
        {
            "img": "foto1.jpg",
            "texto": "Essa foi a vez em que vc raspou minha barbinha pq vc disse q tava grande e pediu para raspar meu amor"
        },
        {
            "img": "foto2.jpg",
            "texto": "essa vez vc tava dormindo abraçadinha cmg bem apertado e espero mto q isso volte a se repetir onde vc esteja confortável"
        },
        {
            "img": "foto3.jpg",
            "texto": "Essa aqui é a foto q eu mais amo nossa, não preciso dizer mto pois acho q é autoexplicativo"
        },
        {
            "img": "foto4.jpg",
            "texto": "Essa foto é a q eu mais amo, pois vc está muito linda e toda vez q vejo me apaixono pelo seu sorriso novamente, eu simplesmente amo essa foto e ela foi no dia em que fomos comer lanche, vc é a mulher mais linda q existe meu amor, eu te amo !"
        }
    ]

    return render_template("index.html", fotos=fotos)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)