import pytube
import shutil


print('\nCole o Link do video aqui: ')
link = input()

def baixar(link, extencao):
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
    print('\n')
    caminho_original =r'D:\Brincadeiras em Python\{}.mp4'.format(titulo)# Caminho Depois de baixar
    caminho_novo = r'C:\Users\leona\Downloads\{}'.format(titulo)#Pasta Downloads
    caminho_novo = caminho_novo+extencao
    print(caminho_novo,' ',caminho_original)
    shutil.move(caminho_original,caminho_novo)# Movendo o video
    print(f'\n\nVocê pode ver o arquivo em {caminho_novo}\n\n') #Local completo do video

baixar(link,'.mp3')
baixar(link,'.mp4')