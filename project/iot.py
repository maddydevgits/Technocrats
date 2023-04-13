import time
from datetime import datetime
import serial
import time
import telebot

bot=telebot.TeleBot('6055874264:AAHKOZOmB8ouO2oIWGl1ow7qp5-QJitpQu0')
chat_id='5064620560'

ser=serial.Serial('COM3',9600,timeout=0.5)
ser.close()
ser.open()

while True:
    f=open('log.txt','r')
    k=f.read()
    #print(k)
    f.close()

    if(k=='on'):
        ser.write('on'.encode('utf-8'))
        time.sleep(1)
        bot.send_message(chat_id,"Motion Detected at "+str(datetime.now()))
        print('Alert'+str(datetime.now()))
        f=open('log.txt','w')
        f.write('off')
        f.close()
        ser.write('off'.encode('utf-8'))
        time.sleep(1)
