#Escreva uma função em Python que, dado um número PID, imprima o nome do usuário proprietário, o tempo de criação e o uso de memória em KB.
import psutil,time

pid = int(input())
arquivo = psutil.Process(pid)
print(arquivo.name())
print("Usuario:",arquivo.username())
print("Tempo de criação:",time.ctime(arquivo.create_time()))
print("Memoria VMS e RSS:",arquivo.memory_info()[0]/1024,"KB",arquivo.memory_info()[1]/1024,"KB")