#Escreva um programa em Python usando o módulo ‘psutil’, que imprima para a partição corrente:
#o nome do dispositivo,
#o tipo de sistema de arquivos que ela possui (FAT, NTFS, EXT, ...),
#o total de armazenamento em GB e
#o armazenamento disponível em GB.
import psutil

discos = psutil.disk_partitions()
path = discos[0][0]
boot = discos[0]
print("Nome do dispositivo:",boot[0])
print("Sistema de arquivos:",boot[2])
uso_do_disco = psutil.disk_usage(path)
print("Total de armazenamento:",uso_do_disco[0]/1024/1024/1024)
print("Espaço livre:",uso_do_disco[2]/1024/1024/1024,"GB")
