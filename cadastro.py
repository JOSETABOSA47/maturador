import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial
from tkinter import *
import tkinter.messagebox as messagebox
import re
import os
import shutil
from app import WhatsAppBotApp
import time


def wait_element(by, elemento, webdriver):
    print(f'Tentando encontrar "{elemento}" by {by}')
    if webdriver.find_elements(by, elemento):
        return True
    return False


def executar_cadastro(numero):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument('lang=pt-br')
        options.add_argument(f'--user-data-dir=./utils/sessions/{numero}')

        driver = webdriver.Chrome(options=options)

        driver.get("https://web.whatsapp.com/")

        wdw = WebDriverWait(driver, 300, poll_frequency=2)

        esperar_carregar_whatsapp = partial(
            wait_element, By.XPATH, "//*[@id='pane-side']/div/div/div/div[11]")

        wdw.until(esperar_carregar_whatsapp, 'Erro ao carregar whatsapp.')
        time.sleep(10)
        driver.quit()

    except Exception as e:
        print(f"Erro ao executar o cadastro: {e}")


def validate_input():
    texto = campo_entrada.get()
    if re.match(r'^\d{10}$', texto) or re.match(r'^\d{11}$', texto):
        executar_cadastro(numero=texto)
    else:
        messagebox.showwarning(
            "Aviso", "Número incorreto, exemplo: 99999999999")


home = Tk()
home.title("Maturador")
home.minsize(500, 500)

label = Label(home, text="WhatsApp")
label.grid(column=1, row=2, padx=10, pady=20)

campo_entrada = Entry(home)
campo_entrada.grid(column=2, row=2, pady=20)

botao_cadastro = Button(home, text="Cadastrar", command=validate_input)
botao_cadastro.grid(column=3, row=2, padx=10, pady=20, sticky="ew")


def listar_pastas(diretorio):
    pastas = [item for item in os.listdir(
        diretorio) if os.path.isdir(os.path.join(diretorio, item))]
    return pastas


def preencher_select():
    diretorio = "./utils/sessions"
    pastas = listar_pastas(diretorio)

    for pasta in pastas:
        select.insert(END, pasta)


def apagar_pasta_selecionada():
    indice_selecionado = select.curselection()

    if indice_selecionado:
        pasta_selecionada = select.get(indice_selecionado)

        resposta = messagebox.askokcancel(
            "Confirmação", f"Deseja realmente apagar a pasta '{pasta_selecionada}'?")

        if resposta:
            select.delete(indice_selecionado)
            diretorio = "/utils/sessions"
            caminho_pasta = os.path.join(diretorio, pasta_selecionada)
            shutil.rmtree(caminho_pasta)

            messagebox.showinfo(
                "Sucesso", f"A pasta '{pasta_selecionada}' foi apagada com sucesso!")
    else:
        messagebox.showwarning("Aviso", "Nenhuma pasta selecionada.")


linha_separacao = Frame(home, bg='gray', height=2)
linha_separacao.grid(row=3, columnspan=10, sticky='ew', padx=10, pady=10)

select = Listbox(home)
select.grid(column=2, row=5, pady=10)

preencher_select()
botao_apagar = Button(home, text="Apagar Sessão",
                      command=apagar_pasta_selecionada)
botao_apagar.grid(column=3, row=5, padx=10, pady=20)

linha_separacao1 = Frame(home, bg='gray', height=2)
linha_separacao1.grid(row=6, columnspan=10, sticky='ew', padx=10, pady=10)

home.mainloop()
