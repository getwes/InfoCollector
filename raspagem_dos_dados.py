#Imports
from selenium import webdriver
from selenium.webdriver.common.by import By

#Acessar o site https://www.novaliderinformatica.com.br/computadores
driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/placa-de-video')

#Coletando os nomes dos produtos
titulos = driver.find_elements(By.XPATH,"//div[@class='product-name']")

#Coletando os preços dos produtos
precos = driver.find_elements(By.XPATH,"//span[@class='price-off']")

for titulo, preco in zip(titulos, precos):
    print([titulo.text,preco.text])