import pyautogui
import time 
pyautogui.PAUSE = 0.5
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

#Abrir NavegadOR
pyautogui.press ("win")
pyautogui.write ("chrome")  
pyautogui.press ("enter")


#ENTRAR NO SITE
pyautogui.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press ("enter")
time.sleep(3)

#FAZER LOGUIN
pyautogui.click (x=721, y=379)
pyautogui.write ("cliquevantagemkt@gmail.com")
pyautogui.press ("tab")
pyautogui.write ("kkkkkkk") 
pyautogui.click(x=950, y=524) # clique no botao de login
time.sleep(3)


#CADASTRAR PRODUTO
import pandas as pd
print("antes da tabela")
tabela = pd.read_csv("produtos1.csv")
print("depoisdatabela")
print(tabela)
exit()
for linha in tabela.index:
    pyautogui.click (x=719, y=263) 
 # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim