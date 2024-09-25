import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Ler a planilha Excel
df = pd.read_excel('script/planilha_teste.xlsx')

# Configurar o caminho do chromedriver
chrome_driver_path = "/usr/lib/chromium-browser/chromedriver"

# Inicializar o navegador Chrome
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Abrir a página onde os campos serão preenchidos
driver.get('file:///home/crija/Desktop/automatizar_preenchimento_fomulario/formulario.html')

# Esperar um tempo para a página carregar
time.sleep(1)

# Preencher campos com dados da planilha
for index, row in df.iterrows():

    # Localizar e preencher o campo nome, telefone e email.
    nome_input = driver.find_element(By.ID, 'nome')
    email_input = driver.find_element(By.ID, 'email')
    telefone_input = driver.find_element(By.ID, 'telefone')
    
    nome_input.clear()
    nome_input.send_keys(row['Nome'])

    email_input.clear()
    email_input.send_keys(row['Email'])

    telefone_input.clear()
    telefone_input.send_keys(row['Telefone'])

    # Tempo que a página ficará aberta
    time.sleep(2)

driver.quit()