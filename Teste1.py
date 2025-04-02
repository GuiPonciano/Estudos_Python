from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from zipfile import ZipFile
import os
from os.path import basename

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option('prefs', {
    "download.default_directory":r"C:\Users\Yamate TGL\OneDrive\Desktop\Testes-de-Nivelamento\Arquivos_PDF",
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True})

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')
time.sleep(3)

#Aceitando Cookies
xpath_aceitar = '/html/body/div[5]/div/div/div/div/div[2]/button[3]'
aceitar = driver.find_element(By.XPATH, xpath_aceitar)
aceitar.click()
#baixando Pdf
xpath_anexo1 = '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]'
anexo1 = driver.find_element(By.XPATH, xpath_anexo1)
anexo1.click()
#baixando pdf
xpath_anoxo2 = '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[2]/a'
anexo2 = driver.find_element(By.XPATH, xpath_anoxo2)
anexo2.click()
time.sleep(7)

with ZipFile ('Arquivos.zip', 'w') as zipObj:
    for folderName,subfolders,filenames in os.walk(r"C:\Users\Yamate TGL\OneDrive\Desktop\Testes-de-Nivelamento\Arquivos_PDF"):
        for filename in filenames:
            filepath = os.path.join(folderName, filename)
            zipObj.write(filepath, basename(filepath))

