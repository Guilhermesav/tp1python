#Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de armazenamento disponível há na partição do sistema (onde o sistema está instalado).
import psutil
discos =  psutil.disk_partitions()
path = discos[0][0]

uso = psutil.disk_usage(path)
print("Espaço livre:",uso[2]/1024/1024/1024,"GB")