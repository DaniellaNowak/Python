import pyautogui
import time

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar uma tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no site da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o Chrome

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# digitar o site

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# esperar 3 segundos

time.sleep(3)


# Passo 2: Fazer login
# preencher e-mail 


pyautogui.click(x=557, y=374)
pyautogui.write("daninowaktec01@gmail.com")

# preencher senha

pyautogui.press("tab")
pyautogui.write("danitec2025")

# botão de logar

pyautogui.press("tab")
pyautogui.press("enter")

# espera de 3s
time.sleep(3)


# Passo 3: Importar base de dados

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)


# Passo 4: Cadastrar 1 produto
for linha in tabela.index:  # para cada linha da minha tabela

    pyautogui.click(x=526, y=258)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")  # passar para o proximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")  # passar para o proximo campo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")  # passar para o proximo campo
    categoria = str(tabela.loc[linha, "categoria"])  # string = texto -> str
    pyautogui.write(categoria)

    pyautogui.press("tab")  # passar para o proximo campo
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")  # passar para o proximo campo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")  # passar para o proximo campo
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)    



    pyautogui.press("tab")  # passar para o botao enviar
    pyautogui.press("enter")

    pyautogui.scroll(10000)


# Passo 5: Repetir para todos os produtos

