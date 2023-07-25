import threading
import tkinter as tk
from whatsapp import whatsapp, browser, lista_maturacao
import os


class WhatsAppBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Bot")
        self.numeros_telefone = []
        self.lista_numeros_maturacao = []
        self.diretorio = "./utils/sessions"
        self.pastas = [item for item in os.listdir(
            self.diretorio) if os.path.isdir(os.path.join(self.diretorio, item))]
        for x in self.pastas:
            self.numeros_telefone.append((x, x[3:]))
            self.lista_numeros_maturacao.append(x[3:])

        self.start_button = tk.Button(
            self.root, text="Iniciar Bot", command=self.start_threads)
        self.start_button.pack()

    def executar_whatsapp(self, session, telefone_conectado):
        lista_atualizada = lista_maturacao(
            telefone_conectado=telefone_conectado, lista_numeros_maturacao=self.lista_numeros_maturacao)
        options = browser(session=session)
        whatsapp(options=options, lista_maturacao=lista_atualizada)

    def start_threads(self):
        threads = []
        for session, telefone_conectado in self.numeros_telefone:
            t = threading.Thread(target=self.executar_whatsapp,
                                 args=(session, telefone_conectado))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()


if __name__ == '__main__':
    root = tk.Tk()
    app = WhatsAppBotApp(root)
    root.mainloop()
