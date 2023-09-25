"""
Esse codigo envia mensagem em massa para varios numeros dentro da lista

By: George Telles
+55 11 93290-7425
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib
import time
import os

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com")

# esperar a tela do whatsapp carregar
while len(navegador.find_elements(By.ID, 'side')) < 1: # -> lista for vazia -> que o elemento não existe ainda
    time.sleep(1)
time.sleep(2) # só uma garantia

# o whatsapp já carregou
import pandas as pd

tabela = pd.read_excel("G:/Meu Drive/2. Documentos/dock/Enviar msg no Whats com Python/Envios.xlsx")
print(tabela[['nome', 'mensagem', 'arquivo']]) # tem também uma coluna telefone dentro da tabela

for linha in tabela.index:
    # enviar uma mensagem para a pessoa
    nome = tabela.loc[linha, "nome"]
    mensagem = tabela.loc[linha, "mensagem"]
    arquivo = tabela.loc[linha, "arquivo"]
    telefone = tabela.loc[linha, "telefone"]
    
    texto = mensagem.replace("fulano", nome)
    #codifica o texto para a url
    texto = urllib.parse.quote(texto)

    # enviar a mensagem
    link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
    
    navegador.get(link)
    # esperar a tela do whatsapp carregar -> espera um elemento que só existe na tela já carregada aparecer
    while len(navegador.find_elements(By.ID, 'side')) < 1: # -> lista for vazia -> que o elemento não existe ainda
        time.sleep(2)
    time.sleep(5) # só uma garantia
    
    # você tem que verificar se o número é inválido
    if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
        # enviar a mensagem
        time.sleep(2)
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        
        if arquivo != "N":
            caminho_completo = os.path.abspath(f"G:/Meu Drive/2. Documentos/dock/Enviar msg no Whats com Python/{arquivo}")
            time.sleep(2)
            navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
            time.sleep(2)
            navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[1]/li/div/input').send_keys(caminho_completo)
            time.sleep(3)
            navegador.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
            
        time.sleep(5)
