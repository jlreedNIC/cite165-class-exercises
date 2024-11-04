# -----------
#
# @file     listener.py
# @date     November, 2024
# @class    CITE 165
# @brief    Code to handle setting up a listener for MQTT server
# 
# ------

from messaging import MQTT_Connector

teacher = MQTT_Connector("Teacher", ["cite165"], True)
teacher.connect_MQTT()

try:
    teacher.loop_start()

    while True:
        pass
except KeyboardInterrupt as ke:
    print(f'\nStopping program...')
    teacher.disconnect()