
# 🎮 Jogo "Adivinhe o Número Mágico" (versão web com Flask)<div align="center">
![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)

Um jogo web com Python + Flask, onde o jogador (ou dois jogadores) tentam adivinhar um número sorteado entre 1 e 100.


# Funciona assim: 👇

1. O sistema sorteia um número mágico secreto.

2. O jogador tem no máximo 7 tentativas para acertar.

3. A cada tentativa, o jogo diz se o número é maior ou menor.

4. Se acertar, ganha pontos conforme a tentativa:

   1ª tentativa = 100 pontos

   2ª = 90 pontos

   ... até 7ª = 40 pontos

   Se errar tudo = 0 ponto

5. O jogo pode ser jogado por 1 ou 2 jogadores (alternando).

6. No final, o jogo mostra um ranking com os melhores jogadores, com a pontuação de cada um.

7. O ranking é salvo automaticamente em um arquivo .txt.

# 🧠 Como jogar (via navegador)

1. Acesse http://127.0.0.1:5000/

2. Digite os nomes dos dois jogadores.

3. A cada rodada, um jogador faz um palpite.

4. O sistema informa se o número mágico é maior ou menor.

5. Quem acertar primeiro vence com mais pontos.

6. Se ninguém acertar, vence quem chegar mais perto.

7. O ranking final será salvo no arquivo ranking.txt.

# 🖥️ A interface:

Feita com HTML + CSS 

Mostra as regras do jogo, o formulário para jogar e o ranking final.

Tem botão de jogar novamente.

# ⚙️ Tecnologias usadas:

Python para a lógica do jogo.

Flask para transformar o jogo em um site.

HTML + CSS para a interface visual.

Arquivo ranking.txt para salvar os resultados.

# 📦  Execução

### Rode o servidor Flask
python app.py


# 💬 Contato
Desenvolvido por Moacir S Neto

