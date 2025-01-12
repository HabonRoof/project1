"""
File name: project1.py
Author: Johnson Chen
Description: To practive pyhton language
Date: 2025/01/12
This file will change to familiar python script and most used library
with copilot
"""

import ntplib
from time import ctime, sleep, strftime, strptime


def get_ntp_time():
    client = ntplib.NTPClient()
    response = client.request('cn.pool.ntp.org')
    return ctime(response.tx_time)

def check_alarm(alarm_time):
    current_time = strftime('%H:%M:%S', strptime(get_ntp_time()))
    return current_time == alarm_time

alarm_time = '09:01:00'

while(True):
    
    if check_alarm(alarm_time) :
        print('\n ALARM is ringing')
        break
    else:
        print(f'Curent NTP time is {get_ntp_time()}')

    sleep(1)
