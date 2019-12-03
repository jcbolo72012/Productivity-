#written by John Bolognino in python 2.7.17 (for some godforsaken reason)

from task import *
import os

print("Welcome to productivity suite, where we measure how fast you do tasks and how long it will take you to do them")
units = input("what are the units of your task?")
goal = int(input("how many units would you like to set as your goal?"))
unit = input("What unit of time would you like to measure in? ((S)econds, (M)inutes, or (H)ours)").lower()
timegoal = int(input("How much time would you like to complete the whole task in? (in the unit you just set)"))
breaks = input("Would you like to schedule breaks into your work?(y/n)").lower()
breakfreq = 0
breaklength = 0
if breaks == 'y':
    breaklength = float(input("how long would you like each break to be? (in minutes)"))
    breakfreq = int(input("how many units would you like to complete between each break?"))
else:
    pass

t = Task(units, goal, unit, breakfreq, breaklength, timegoal)

while True:
    print(t)
    now = time.time()
    print("You'll be done at: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now + t.time_to_reach_goal())))
    quit = input("press enter to log a unit completed, type 'q' and press enter to quit").lower()
    timer = time.time() - now
    t.update_time(timer)
    if quit == 'q':
        break
    if t.complete == t.goal:
        quit = raw_input("Congrats! You did all the units of your task! That means its done wooohoooooooo, press enter to end this madness")
        break
    if t.break_frequency !=0 :
        if t.complete % t.break_frequency == 0:
            print("relax! you're on break until " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end)))
            time.sleep(60*t)
    os.system('cls' if os.name == 'nt' else 'clear')
