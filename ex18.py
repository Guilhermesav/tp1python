#Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de memória principal e quanto de memória de paginação (swap) existem no computador.
import psutil
memoria = psutil.virtual_memory()
print("Memoria principal:",memoria[0]/1024/1024/1024,"GB")
memoria_swap = psutil.swap_memory()
print("Memoria swap:",memoria_swap[0]/1024/1024/1024,"GB")