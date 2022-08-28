"""
Módulo Principal
Descrição: Este programa organiza os arquivos de uma pasta de acordo com sua extensão, movendo-os para as pastas Documentos e/ou Planilhas
conforme for o caso.
Autor: Carlos Rafael Batista Santos
Data: 28/08/2022
Versão: 1.0.0
"""

# Importação de módulos

import os
import shutil



# Definição de funções

def main():
    # Instanciação das Listas
    lista_arquivos = []
    lista_planilhas = []
    lista_documentos = []
    

    # Entrada
    lista_arquivos = os.listdir('Pasta/')
    print(f"Arquivos no diretório Pasta/", os.listdir('Pasta/'))


    # Processamento
    for arquivo in lista_arquivos:
        if ".xls" in arquivo:
            lista_planilhas.append(arquivo)
        if ".doc" in arquivo:        
            lista_documentos.append(arquivo)                
                
    if len(lista_planilhas) > 0:
        os.makedirs('Pasta/Planilhas/')
        for arquivo in lista_planilhas:
            shutil.move(f"Pasta/{arquivo}", f"Pasta/Planilhas/{arquivo}")
    if len(lista_documentos) > 0:
        os.makedirs('Pasta/Documentos/')
        for arquivo in lista_documentos:
            shutil.move(f"Pasta/{arquivo}", f"Pasta/Documentos/{arquivo}") 


    # Saída
    print(f"Pasta Atual", os.getcwd())
    print(f"Arquivos no diretório Pasta/", os.listdir('Pasta/'))
    print(f"Arquivos no diretório Planilhas/", os.listdir('Pasta/Planilhas/'))
    print(f"Arquivos no diretório Documentos/", os.listdir('Pasta/Documentos/'))

 
# Execução do programa

if __name__ == "__main__":
    main()
