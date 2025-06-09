import pyautogui
pyautogui.FAILSAFE = True

import time

#pyautogui.click - clicar em algum lugar
#pyautogui.press - apertar 1 tecla 
#pyautogui.write - escrever um texto
#pyautogui.hotkey- apertar uma combinação de teclas 

pyautogui.PAUSE = 0.5
# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o Chrome 
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter') 
time.sleep (1)
# Digitar o site 
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(2)
# Passo 2: Fazer login
pyautogui.click(x=645, y=384)
pyautogui.write('rskeila@outlook.com')
time.sleep (0.5)
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.write('123654')
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(0.5)
# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv") 
print(tabela)

# Passo 4: Cadastrar 1 produto
for linha in tabela.index: #Para cada linha da minha tabela
    
    pyautogui.click(x=756, y=258)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press ("tab") 
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":    

        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(1000)
# Passo 5: Repetir para todos os produtos 
# Pyautogui: Fazer automação com Python 
