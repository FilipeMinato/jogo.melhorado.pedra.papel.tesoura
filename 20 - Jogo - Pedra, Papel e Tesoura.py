# Projeto 14 - Pedra, Papel e Tesoura com Repetição
# Jogo interativo onde o jogador enfrenta o computador em várias rodadas.
# O placar é exibido ao final de cada rodada, com mensagens divertidas.
# Usa interface gráfica com Tkinter e lógica simples de comparação.

import tkinter as tk
from tkinter import messagebox
import random

class PedraPapelTesoura:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo: Pedra, Papel e Tesoura")  # Título da janela
        self.root.geometry("400x450")  # Tamanho fixo
        self.root.resizable(False, False)  # Janela não redimensionável

        # Opções possíveis
        self.opcoes = ['pedra', 'papel', 'tesoura']

        # Variáveis de pontuação
        self.placar_usuario = 0
        self.placar_computador = 0
        self.empates = 0

        # Criação dos elementos da interface
        self.criar_interface()

    def criar_interface(self):
        """
        Cria os widgets gráficos e os posiciona na janela.
        """
        # Título principal
        self.label_titulo = tk.Label(self.root, text="🪨 Pedra, 📄 Papel ou ✂️ Tesoura?", font=("Arial", 16, "bold"))
        self.label_titulo.pack(pady=10)

        # Regras do jogo
        self.label_regras = tk.Label(self.root, text="Escolha uma das opções abaixo para desafiar o computador.\n"
                                                     "Vença ele se for capaz! 😎", font=("Arial", 10), justify="center")
        self.label_regras.pack(pady=10)

        # Botões das jogadas
        self.frame_botoes = tk.Frame(self.root)
        self.frame_botoes.pack(pady=10)

        self.btn_pedra = tk.Button(self.frame_botoes, text="🪨 Pedra", width=10, command=lambda: self.jogar("pedra"))
        self.btn_papel = tk.Button(self.frame_botoes, text="📄 Papel", width=10, command=lambda: self.jogar("papel"))
        self.btn_tesoura = tk.Button(self.frame_botoes, text="✂️ Tesoura", width=10, command=lambda: self.jogar("tesoura"))

        self.btn_pedra.grid(row=0, column=0, padx=5)
        self.btn_papel.grid(row=0, column=1, padx=5)
        self.btn_tesoura.grid(row=0, column=2, padx=5)

        # Resultado da rodada
        self.label_resultado = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.label_resultado.pack(pady=15)

        # Placar atual
        self.label_placar = tk.Label(self.root, text=self.get_placar(), font=("Arial", 12, "bold"))
        self.label_placar.pack(pady=10)

    def jogar(self, jogador):
        """
        Lógica principal do jogo: define a jogada do computador e compara com a do jogador.
        """
        computador = random.choice(self.opcoes)  # Escolha aleatória do computador

        # Mensagem base com escolhas
        resultado_texto = f"Você escolheu: {jogador.capitalize()}\nComputador escolheu: {computador.capitalize()}\n\n"

        # Verifica o resultado da rodada
        if jogador == computador:
            resultado_texto += "Empate! Parece que vocês pensam igual 😅"
            self.empates += 1
        elif (jogador == 'pedra' and computador == 'tesoura') or \
             (jogador == 'papel' and computador == 'pedra') or \
             (jogador == 'tesoura' and computador == 'papel'):
            resultado_texto += "Você venceu essa! O computador está ficando bravo 😤"
            self.placar_usuario += 1
        else:
            resultado_texto += "Computador venceu essa... ele está se achando agora 😎"
            self.placar_computador += 1

        # Exibe resultado na interface
        self.label_resultado.config(text=resultado_texto)
        self.label_placar.config(text=self.get_placar())

        # Pergunta se o usuário quer jogar novamente
        self.perguntar_novamente()

    def get_placar(self):
        """
        Retorna o placar formatado como string.
        """
        return f"Placar: Você {self.placar_usuario} x {self.placar_computador} Computador | Empates: {self.empates}"

    def perguntar_novamente(self):
        """
        Abre uma janela perguntando se o jogador quer jogar outra rodada.
        """
        resposta = messagebox.askyesno("Jogar novamente?", "Deseja jogar mais uma rodada?")
        if not resposta:
            self.mostrar_resultado_final()
            self.root.quit()  # Fecha a janela

    def mostrar_resultado_final(self):
        """
        Mostra o resultado final do jogo e uma mensagem divertida com base no placar.
        """
        msg_final = f"Placar Final: Você {self.placar_usuario} x {self.placar_computador} Computador\nEmpates: {self.empates}\n\n"
        if self.placar_usuario > self.placar_computador:
            msg_final += "Parabéns! Você humilhou a máquina! 🏆"
        elif self.placar_usuario < self.placar_computador:
            msg_final += "O computador venceu... mas só porque ele joga muito! 🤖"
        else:
            msg_final += "Empate técnico! Dois mestres do jogo! 🤝"

        messagebox.showinfo("Fim de Jogo", msg_final)


# ===============================
# Execução da aplicação
# ===============================
if __name__ == "__main__":
    root = tk.Tk()
    app = PedraPapelTesoura(root)
    root.mainloop()
