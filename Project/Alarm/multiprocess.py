import multiprocessing
from playsound import playsound

p = multiprocessing.Process(target=playsound, args=("/Programma_Alarm_morning_alarm.mp3",))
p.start()
input("press ENTER to stop playback")
p.terminate()