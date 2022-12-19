import instaloader
import instagrapi
import os
import getpass
import time
import random

print("""
   __     _ _                              
  / _|   (_) |                             
 | |_ ___ _| |_ ___    _ __   ___  _ __    
 |  _/ _ \ | __/ _ \  | '_ \ / _ \| '__|   
 | ||  __/ | || (_) | | |_) | (_) | |      
 |_|_\___|_|\__\___/  | .__/ \___/|_|      
 |_   _|              | |                  
   | |  ___ _ __ __ _ |_|  ___  __ _  __ _ 
   | | / __| '__/ _` / __|/ _ \/ _` |/ _` |
  _| |_\__ \ | | (_| \__ \  __/ (_| | (_| |
 |_____|___/_|  \__,_|___/\___|\__, |\__,_|
                                __/ |      
                               |___/       
""")

hashtags = "#meme #casal #fofoca #choquei #safadeza #memes #love #amor #novela #humor #segundosol #rafakalimann #brasil #casamento #midia #safados #comedia #photography #otemponãopara #like #edsoncelulari #instalove #instagood #fotografia #espalhealuz #funny #wedding #otemponaopara #trendingtopic #brazil"
listadehashtags = [i for i in hashtags.split(" ")]
legenda = "SIGA A PÁGINA PARA MAIS CONTEÚDO :D\n\n"
horarios = ["22:15:00", "21:10:00", "23:59:00",
 "01:15:00", "03:00:00", "04:15:00",
 "05:30:00", "07:00:00", "08:30:00",
 "10:00:00", "11:30:00", "13:00:00",
 "14:30:00", "16:00:00", "17:30:00",
 "19:00:00"]

def baixafotos():
    il = instaloader.Instaloader()
    nomedapagina = input("Insira o nome da página da qual deseja baixar as fotos: ")
    posts = instaloader.Profile.from_username(il.context, nomedapagina).get_posts()
    contagem = 0
    for post in posts:
        if post.is_video == True:
            print("É video!\n")
        else:
            il.download_pic(url=post.url, filename=nomedapagina+str(contagem), mtime=post.date_local)
            contagem += 1

def uploadfotos():
    usuario = str(input("Digite o usuário de login: "))
    senha = str(getpass.getpass("Digite a senha de login: "))
    listanaofoi = os.listdir('naofoi')
    while True:
        agr = time.localtime()
        current_time = time.strftime("%H:%M:%S", agr)
        if current_time in horarios:
            ig = instagrapi.Client()
            ig.login(usuario, senha)
            foto = random.choice(listanaofoi)
            path = 'naofoi/'+foto
            ig.photo_upload(path, caption=legenda+hashtags, extra_data={"like_and_view_counts_disabled": 1})
            os.replace(path, 'jafoi/'+foto)
            print("Foto postada com sucesso!")
            print("Aguardando horario para postagem da próxima foto!")
            ig.logout()
            time.sleep(120)

if __name__ == "__main__":
    print("""
    ########################
         Menu de Opções
      1. Baixar fotos de alguma página
      2. Upload automático de fotos
    ########################
    """)
    opcao = int(input("Digite o número da opção desejada: "))
    if opcao == 1:
        baixafotos()
    elif opcao == 2:
        uploadfotos()

