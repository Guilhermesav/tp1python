#Escreva um programa que imprima apenas o caminho absoluto de um arquivo com nome relativo. A impressão não deve conter o nome do arquivo, apenas o caminho.
import os

arquivo = "arqteste.txt"

caminho = os.path.abspath(arquivo)

separacao =  os.path.split(caminho)

print(separacao[0])
