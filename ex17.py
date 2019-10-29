#Escreva um programa em Python, usando o módulo ‘psutil’, que imprima 20 vezes, de segundo a segundo, o percentual do uso de CPU do computador.
import psutil
for i in range(0,20):
    print(psutil.cpu_percent(interval = 1,percpu =  True))