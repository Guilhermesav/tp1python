#Usando o módulo ‘subprocess’ de Python, crie um processo externo e imprima o PID dele.
import subprocess, os,psutil
print(os.getcwd())
arquivo = subprocess.Popen(["notepad","arqteste.txt"])

print("PID:",arquivo.pid)
