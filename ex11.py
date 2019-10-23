#Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo, usando o módulo ‘os’, de bloco de notas (notepad) para abri-lo.
import os

nome_do_arquivo = input()

if os.path.exists(nome_do_arquivo):
    os.system(nome_do_arquivo)
else:
    print("este arquivo não existe")

