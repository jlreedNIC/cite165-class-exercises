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

# allows for moving of the submit.py file and still finding library
sys.path.append(os.getcwd() + "/cite165-class-exercises/submission")
sys.path.append(os.getcwd() + "/.cite165-class-exercises/submission")

from messaging import MQTT_Connector
import datetime

def grab_guess(question:str):
    """
    Grab input from the terminal based on a question to ask.

    :param question: string, prompt to ask
    :return: capitalized version of input
    """
    choice = 'n'
    while choice != 'y' and choice != 'yes':
        answer = input(f'\n{question} _ ')
        choice = input(f"{answer}. Is this correct? y/n _ ")
        choice = choice.lower()
    
    answer = answer.capitalize()
    return answer

print("Congratulations for completing the activity. There are a few questions you should answer.")
guess = {}

timestamp = datetime.datetime.now()
guess["time"] = timestamp

# name
guess['student_name'] = grab_guess("What is your name?")

# killer guess
guess['killer_guess'] = grab_guess("What is the name of the cereal killer?")

# attack location guess
guess['location'] = grab_guess("Where is the cereal killer going to attack next?")

# home base guess
guess['home'] = grab_guess("Bonus! Where is his home base?")

# leader guess
guess['leader'] = grab_guess("Bonus! Who is really in charge?")


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