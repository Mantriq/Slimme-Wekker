import imp
from operator import truediv
from winsound import PlaySound
from xmlrpc.client import DateTime
from playsound import playsound
from time import strftime
import multiprocessing



alarm_time = input("Enter the time you want to wake up (HH:MM:SS): ")



alarm_hours = alarm_time[0:2]
alarm_minutes = alarm_time[3:5]
alarm_sec = alarm_time[6:9]




alarm_hours = alarm_time[0:2]
alarm_minutes = alarm_time[3:5]
alarm_sec = alarm_time[6:9]

while True:

    now = strftime('%H:%M:%S')

    current_hour = strftime('%H')
    current_min = strftime('%M')
    current_sec = strftime('%S')


    if alarm_hours == current_hour:
        if alarm_minutes == current_min:
            if alarm_sec == current_sec:
                print("wake up")

                p = multiprocessing.Process(target=playsound, args=("C:\\Users\\Senne\\Downloads\\morning_alarm.mp3",))
                p.start()
                trash = input("Press enter to stop the alarm")
                p.terminate()

                break

                
                






 
    



