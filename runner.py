import requests
import datetime
import time
ft = True
while 1:
    if ft:
        print('Runner INITIALIZED')
        ft = False
    dt = datetime.datetime.now()
    hour = dt.hour
    if hour > 8 and hour < 17: #During day
        print('Tuning off lights periodically')
        req = requests.get('http://192.168.0.83/2/on')
        req = requests.get('http://192.168.0.83/3/on')
        req = requests.get('http://192.168.0.83/4/on')
        time.sleep(120)
    elif hour > 11 and hour < 4: #During night
        print('Tuning off lights periodically')
        req = requests.get('http://192.168.0.83/2/on')
        req = requests.get('http://192.168.0.83/3/on')
        req = requests.get('http://192.168.0.83/4/on')
        time.sleep(120)
