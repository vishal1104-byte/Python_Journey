from playsound import playsound
import time

CLEAR = "\033[2J"                           # This is the code that clear the full terminal and terminal looks blank 
CLEAR_AND_RETURN = "\033[H"                 # This will give the timer at a place 

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d} ")                # this :02d is used to format the timer as 01:02

    playsound("alarm.mp3")

minutes = int(input("ENter the minutes or second you want to set your alarm"))
alarm(minutes)