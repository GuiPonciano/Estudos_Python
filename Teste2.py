from PyPDF2 import PdfReader
import tabula
import csv
from zipfile import ZipFile
import os
from os.path import basename

with open(r"C:\Users\Yamate TGL\OneDrive\Desktop\Testes-de-Nivelamento\Arquivos_PDF\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf", 'rb') as pdf_file:
    pdf_reader = PdfReader(pdf_file)

    num_pages = len(pdf_reader.pages)

    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]

        text = page.extract_text()

pdf_path = r"C:\Users\Yamate TGL\OneDrive\Desktop\Testes-de-Nivelamento\Arquivos_PDF\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

tabelas = tabula.read_pdf(pdf_path, pages="all")

with open('Anexo.I.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo, delimiter=';')

    for i, tabela in enumerate(tabelas):
        escritor_csv.writerow(tabela.columns.tolist())
        escritor_csv.writerows(tabela.values.tolist())
        escritor_csv.writerow([])

with ZipFile ("Teste_GUILHERME.zip", 'w') as zipObj:
    for folderName,subfolders,filenames in os.walk(r"C:\Users\Yamate TGL\OneDrive\Desktop\Testes-de-Nivelamento\Arquivos_PDF"):
        for filename in filenames:
            filepath = os.path.join(folderName, filename)
            zipObj.write(filepath, basename(filepath))