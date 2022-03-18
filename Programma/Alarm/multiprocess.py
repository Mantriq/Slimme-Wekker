import multiprocessing
from playsound import playsound

p = multiprocessing.Process(target=playsound, args=("C:\\Users\\Senne\\Downloads\\morning_alarm.mp3",))
p.start()
input("press ENTER to stop playback")
p.terminate()