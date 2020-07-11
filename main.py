import random
import facebook
import time
import schedule

def messageGenerator():
    frases = ["Mas é óbvio que sim", "Com certeza", "O ritual foi cumprido hoje", "Si mi amigo", "Sì mio amico",
                  "Ja mein Freund", "да мой друг", "Claro que sim né", "Mandou com um duplo carpado", "Hoje ele mandou 2 em sequência",
                  "~Não", "Opa","Sim, meu patrão", "Mandou assim que acordou", "Mandou por video-chamada"]
    numera = random.randint(1, 15)
    return frases[numera]

def postToFacebook(token,message="Hello"):
    graph = facebook.GraphAPI(token)
    post_id = graph.put_photo(image = open('400.jpg', 'rb'), message= message)["post_id"]
    print(f"Postou com sucesso n° {post_id}")

def job():
    token = "" ##Insert your token here
    message = messageGenerator()
    postToFacebook(token,message)

if __name__  == '__main__':
    schedule.every(20).hours.do(job).run()
    while True:
        schedule.run_pending()
        time.sleep(1)