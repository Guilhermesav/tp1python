#Escreva um programa que mostre a quantidade de bytes (em KB) de cada arquivo em um diretório.
import os

print(os.listdir()) #diretorio corrente
path = os.listdir()
for i in path:
    tamanho = os.stat(i)
    print(i,tamanho.st_size/1024,"KB")