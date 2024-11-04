# -----------
#
# @file     submit.py
# @date     November, 2024
# @class    CITE 165
# @brief    Code to handle getting student guesses and pushing to an MQTT server.
#
#           This file can be placed in a directory above the home directory so students don't have to navigate in.
# 
# ------

import sys
import os

sys.path.append(os.getcwd() + "/cite165-class-exercises/submission")

from messaging import MQTT_Connector
import datetime


print("Congratulations for completing the activity. There are a few questions you should answer.")
guess = {}

timestamp = datetime.datetime.now()
guess["time"] = timestamp

# name
choice = 'n'
while choice != "y" and choice != "yes" :
    student_name = input("\nWhat is your name? _ ")
    choice = input(f"{student_name}. Is this correct? y/n _ ")
    choice = choice.lower()

guess['student_name'] = student_name.capitalize()

# killer guess
choice = 'n'
while choice != "y" and choice != "yes" :
    killer_guess = input("\nWhat is the name of the cereal killer? _ ")
    choice = input(f"{killer_guess}. Is this correct? y/n _ ")
    choice = choice.lower()

guess['killer_guess'] = killer_guess.capitalize()

# attack location guess
choice = 'n'
while choice != "y" and choice != "yes" :
    location = input("\nWhere is the cereal killer going to attack next? _ ")
    choice = input(f"{location}. Is this correct? y/n _ ")
    choice = choice.lower()

guess['location'] = location.capitalize()

# home base guess
choice = 'n'
while choice != "y" and choice != "yes" :
    home = input("\nBonus! Where is his home base? _ ")
    choice = input(f"{home}. Is this correct? y/n _ ")
    choice = choice.lower()

guess['home'] = home.capitalize()

# leader guess
choice = 'n'
while choice != "y" and choice != "yes" :
    leader = input("\nBonus! Who is really in charge? _ ")
    choice = input(f"{leader}. Is this correct? y/n _ ")
    choice = choice.lower()

guess['leader'] = leader.capitalize()


formatted_guess = f"""
Date: {guess['time'].strftime('%-I:%M:%S %p')}
Name: {guess['student_name']}
Killer's name: {guess['killer_guess']}
Killer's next move: {guess['location']}
Bonus! Killer's home base: {guess['home']}
Bonus! Real leader: {guess['leader']}
"""

string_guess = f"{guess['time'].strftime('%-I:%M:%S %p'):12} {guess['student_name']:20} {guess['killer_guess']:20} {guess['location']:20} {guess['home']:20} {guess['leader']:10}"

print('Sending submission...')
student = MQTT_Connector("Student")
student.connect_MQTT()

student.loop_start()
student.publishMessage('cite165', string_guess)
print(formatted_guess)

student.loop_stop
student.disconnect()