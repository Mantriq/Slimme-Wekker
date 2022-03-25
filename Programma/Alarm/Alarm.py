import imp
from operator import truediv
from pickle import TRUE
from winsound import PlaySound
from xmlrpc.client import DateTime
from playsound import playsound
from time import strftime
from multiprocessing import Process, Queue
import random



def play():
    playsound("C:\\Users\\Senne\\Downloads\\morning_alarm.mp3")

def calculation():

    # De reken oefening zal een Som zijn

    rand_nr1 = random.randint(0,100)
    rand_nr2 = random.randint(0,100)

    outcome = rand_nr1 + rand_nr2

    print("To turn of the alarm, make this simple equation")

    while TRUE:
        print(rand_nr1, " + ", rand_nr2, ": ")
        user_outcome = input()                   #Uitkomst van de gebruiker

        user_outcome = int(user_outcome)

        if (outcome == user_outcome):
            print("Correct!")
            return
        else:
            print("Wrong, try again.")






if __name__ == "__main__":
    
    alarm_time = input("Enter the time you want to wake up (HH:MM:SS): ")


    queue = Queue()
    sound_process = Process(target=play, args=())


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

                   
                    sound_process.start()
                    print("wake up")

                    calculation()
                    sound_process.terminate()

                    break

                
                






 
    



