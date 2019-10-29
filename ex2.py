#Sobre variáveis de ambiente, responda:
#O que são?
#Um valor dinamico que pode alterar a maneira como o processo é executado no computador
#Como elas podem ser obtidas pelo módulo ‘os’ de Python?
#Por meio da função os.environ
#Como pode ser obtido o caminho completo do diretório de usuário em Python, através das variáveis de ambiente?
#Printando a função os.environ['HOMEDRIVE'] e os.environ['HOMEPATH'] juntas, como no exemplo abaixo. 
import os

print(os.environ['HOMEDRIVE'] + os.environ['HOMEPATH'])

