#Escreva um programa que indique se um arquivo existe ou não. Caso exista, indique se é realmente um arquivo ou não.
import os

arquivo_a_ser_testado = "arqteste.txt"

if os.path.isfile(arquivo_a_ser_testado):
    print(arquivo_a_ser_testado)
else:
    print("Este arquivo não existe")

