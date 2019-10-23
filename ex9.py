#Escreva um programa que mostre as datas de criação e modificação de cada arquivo em um diretório.
import os,time

print(os.listdir()) #diretorio corrente
path = os.listdir()
for i in path:
    status = os.stat(i)
    datac = status.st_ctime
    datam = status.st_mtime
    print(i,"Data de criação",time.ctime(datac))
    print(i,"Data de modificação",time.ctime(datam))