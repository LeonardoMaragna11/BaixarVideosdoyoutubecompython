import pytube

import shutil

extecao = '.mp4'
print('\nCole o Link do video aqui: ')
link = input()
yt = pytube.YouTube(link) #Prepara
titulo = yt.title
print(f'\nBaixando: {titulo}...\n')

ys = yt.streams.get_highest_resolution()#Melhor resolução
ys.download() #Download


#Tirando Caracteres especiais
titulo = titulo.replace('|','')
titulo = titulo.replace('#','')
titulo = titulo.replace('?','')
titulo = titulo.replace(',','')

print('Deseja converter para mp3?')
converter = input()
print('\n')

caminho_original =r'D:\Brincadeiras em Python\{}.mp4'.format(titulo)# Caminho Depois de baixar
caminho_novo = r'C:\Users\leona\Downloads\{}'.format(titulo)#Pasta Downloads

converter = converter.upper()


if converter == 'S' or converter=='SIM':
    extecao = '.mp3'

caminho_novo = caminho_novo+extecao

print(caminho_novo,' ',caminho_original)


shutil.move(caminho_original,caminho_novo)# Movendo o video
print(f'\n\nVocê pode ver o arquivo em {caminho_novo}\n\n') #Local completo do video


#D:\Brincadeiras em Python\Curso de C++ 05 - Declarações múltiplas de variáveis, Constantes Define.mp4
#D:\Brincadeiras em Python\Curso de C++ 05 - Declarações múltiplas de variáveis Constantes Define.mp4
#C:\Users\leona\Downloads\Curso de C++ 05 - Declarações múltiplas de variáveis, Constantes Define.mp4