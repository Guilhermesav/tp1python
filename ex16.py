#Escreva um programa em Python, usando o módulo ‘psutil’, que imprima o tempo de CPU em segundos por núcleo.
import psutil,time
print(time.thread_time())
tempos = psutil.cpu_times(percpu=True)

for cpu in tempos:
    for i in cpu:
        print(int(cpu[i]*1000))
