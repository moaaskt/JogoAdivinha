# Importa as bibliotecas necessárias
from flask import Flask, render_template, request, redirect, url_for  # Flask para criar o site
import random  # Para gerar números aleatórios
import os  # Para trabalhar com arquivos do sistema

# Cria a aplicação Flask (nosso site)
app = Flask(__name__)
app.secret_key = 'segredo_super_secreto'  # Chave secreta para segurança

# Arquivo onde serão salvos os rankings
RANKING_FILE = "ranking.txt"

# Variáveis globais para controlar o jogo:
ranking = []  # Lista para armazenar os rankings
numero_magico = random.randint(1, 100)  # Número que os jogadores devem adivinhar (entre 1 e 100)
tentativas = 0  # Contador de tentativas
modo_jogo = 1  # 1 = 1 jogador, 2 = 2 jogadores
jogador_atual = 1  # Controla qual jogador está jogando (1 ou 2)
jogadores = ["", ""]  # Nomes dos jogadores

# Página inicial do jogo
@app.route("/", methods=["GET", "POST"])
def index():
    global numero_magico, tentativas, ranking, modo_jogo, jogador_atual, jogadores
    
    # Se o usuário enviou o formulário (clicou em iniciar jogo)
    if request.method == "POST":
        # Pega os nomes dos jogadores e o modo do jogo
        nome1 = request.form.get("jogador1")
        nome2 = request.form.get("jogador2")
        modo_jogo = int(request.form.get("modo_jogo"))
        
        # Prepara os jogadores e reinicia o jogo
        jogadores = [nome1, nome2 if nome2 else ""]
        numero_magico = random.randint(1, 100)  # Novo número aleatório
        tentativas = 0  # Zera as tentativas
        jogador_atual = 1  # Começa com o jogador 1
        return redirect(url_for('jogo'))  # Vai para a página do jogo
    
    # Mostra a página inicial (quando acessa o site)
    return render_template("index.html", fase="inicio")

# Página onde o jogo acontece
@app.route("/jogo", methods=["GET", "POST"])
def jogo():
    global numero_magico, tentativas, ranking, modo_jogo, jogador_atual, jogadores
    mensagem = ""  # Mensagem que será mostrada ao jogador
    
    # Se o jogador enviou um palpite
    if request.method == "POST":
        palpite = int(request.form.get("palpite"))  # Pega o número chutado
        tentativas += 1  # Aumenta o contador de tentativas
        nome = jogadores[jogador_atual - 1]  # Pega o nome do jogador atual
        
        # Se acertou o número
        if palpite == numero_magico:
            # Calcula a pontuação (quanto menos tentativas, mais pontos)
            pontos = 100 - (tentativas - 1) * 10
            pontos = max(pontos, 40)  # Pontuação mínima é 40
            mensagem = f"🎉 Parabéns, {nome}! Acertou com {tentativas} tentativa(s). Pontos: {pontos}"
            
            # Salva no ranking
            ranking.append((nome, pontos))
            salvar_ranking()
            
            # Mostra a tela de fim de jogo
            return render_template("index.html", fase="fim", mensagem=mensagem, ranking=carregar_ranking())
        
        # Se errou
        else:
            # Se já fez 7 tentativas (perdeu)
            if tentativas >= 7:
                mensagem = f"❌ Fim de jogo! O número era {numero_magico}."
                ranking.append((nome, 0))  # 0 pontos por perder
                salvar_ranking()
                return render_template("index.html", fase="fim", mensagem=mensagem, ranking=carregar_ranking())
            
            # Dá uma dica (se o número é maior ou menor)
            dica = "maior" if palpite < numero_magico else "menor"
            mensagem = f"Tentativa {tentativas}: O número é {dica} que {palpite}"
            
            # Se for modo 2 jogadores, alterna entre eles
            if modo_jogo == 2:
                jogador_atual = 2 if jogador_atual == 1 else 1
    
    # Mostra a página do jogo
    return render_template("index.html", fase="jogo", tentativas=tentativas, 
                         jogador=jogadores[jogador_atual - 1], mensagem=mensagem)

# Função para salvar o ranking no arquivo
def salvar_ranking():
    global ranking
    # Ordena do maior para o menor pontuador
    ranking.sort(key=lambda x: x[1], reverse=True)
    
    # Escreve no arquivo
    with open(RANKING_FILE, "w") as f:
        for i, (nome, pontos) in enumerate(ranking, 1):
            f.write(f"  {nome}: {pontos} pontos\n")

# Função para carregar o ranking do arquivo
def carregar_ranking():
    # Se o arquivo não existe, retorna lista vazia
    if not os.path.exists(RANKING_FILE):
        return []
    
    # Lê o arquivo e retorna as linhas
    with open(RANKING_FILE, "r") as f:
        return f.readlines()

# Roda o aplicativo se este arquivo for executado diretamente
if __name__ == "__main__":
    app.run(debug=True)  # debug=True mostra erros detalhados
