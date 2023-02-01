import selenium
from selenium import webdriver 
#
# Configuracao abaixo faz com que não haja problemas de compatibilidade de versao, pois o web/geck precisao ser da mesma versao do navegador. 
# Com a configacao, mesmo que surja atualizacoes do navegador, nao sera necessario atualizar o codigo. 
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
services = Service(GeckoDriverManager().install())
navegator = webdriver.Firefox(service=services)
# Configuracao padrao acima, que deve ser repetida sempre que usar o selenium.

navegator.get("https://www.linkedin.com/home")
navegator.find_element('xpath', '//*[@id="session_key"]').send_keys(input('Digitar e-mail: '))
navegator.find_element('xpath', '//*[@id="session_password"]').send_keys(input('Digitar senha: '))
navegator.find_element('xpath', '/html/body/main/section[1]/div/div/form/button').click()

 

