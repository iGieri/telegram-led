import telepot
from nanpy import *
from time import sleep

chat_id=0
txt=""
led_pin=2

try:
    connection=SerialManager()
    a=ArduinoApi(connection=connection)
except:
    print("Non sono riuscito a connettere arduino")

a.pinMode(led_pin,a.OUTPUT)

def attesa():
    global txt
    txt=""
    while txt=="":
        sleep(1)
def on_chat_message (msg):
           global name,txt,chat_id
           print(str(msg)+"\n")
           content_type, chat_type, chat_id=telepot.glance(msg)
           name=msg["from"]["first_name"]
           txt=msg["text"]
           if txt=="/start":
               bot.sendMessage(chat_id,"Benvenuto "+name+" !")
               bot.sendMessage(chat_id,"Scrivi /on per accendere il led")
               bot.sendMessage(chat_id,"Scrivi /off per spegnere il led")

bot=telepot.Bot("634884902:AAEITXu1-E3-EfEtVffRI-xTyznmutqRP1Y")
bot.message_loop(on_chat_message)
while True:
    if txt=="/on":
        #for time in range(1):
            #bot.sendMessage(chat_id,"Led Acceso")
        a.digitalWrite(led_pin,a.HIGH)
    elif txt=="/off":
        #for time in range(1):
            #bot.sendMessage(chat_id,"Led Spento")
        a.digitalWrite(led_pin,a.LOW)
