from datetime import datetime
from pywhatkit import sendwhatmsg_instantly
from pywhatkit.core.exceptions import *

lastminute = -1

def run(number,on):

    global lastminute

    minute = int(datetime.now().minute)
    hour = int(datetime.now().hour)

    if number!="" and on:
        if minute == hour and minute != lastminute:

            lastminute = minute

            try:
                sendwhatmsg_instantly(f"+351{number}", "Toca no chao",wait_time=10, tab_close=True)

                with open("back\log\logs.txt", "a") as log_file:
                    
                    log_file.write(f"[{hour}:{minute}] : Message sent to +351{number}\n")

            except Exception as e:
                with open("back\log\logs.txt", "a") as log_file:
                    
                    log_file.write(f"[{hour}:{minute}] : Failed to send message to +351{number} - {str(e)}\n")
