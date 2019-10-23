#Escreva um programa que indique a extensão de um arquivo usando função do módulo os.path
import os
arquivo = os.path.basename('arq_texto.txt')

arquivo =  arquivo.split('.')

print("A extensão do arquivo é:",arquivo[1])