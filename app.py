from flask import Flask, render_template, request
import random

app = Flask(__name__)
ranking = []

@app.route("/", methods=["GET", "POST"])
def index():
    mensagem = ""
    if request.method == "POST":
        nome = request.form["nome"]
        palpite = int(request.form["palpite"])
        numero = int(request.form["numero_secreto"])
        tentativas = int(request.form["tentativas"]) + 1

        if palpite == numero:
            pontos = 100 - (tentativas - 1) * 10
            mensagem = f"Parabéns, {nome}! Acertou com {tentativas} tentativas. Pontos: {pontos}"
            ranking.append((nome, pontos))
        else:
            dica = "maior" if numero > palpite else "menor"
            mensagem = f"Tentativa {tentativas}: O número é {dica} que {palpite}"

        return render_template("index.html", nome=nome, numero_secreto=numero, tentativas=tentativas, mensagem=mensagem, ranking=ranking)

    return render_template("index.html", nome="", numero_secreto=random.randint(1, 100), tentativas=0, mensagem="", ranking=ranking)

if __name__ == "__main__":
    app.run(debug=True)
