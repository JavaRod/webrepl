import gc
import webrepl
webrepl.start()
gc.collect()

import network
import time

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)

try:
    with open("passwords.txt") as f:
        connections = f.readlines()
except OSError:
    print("No passwords.txt file!")
    connections = []

for n in sta_if.scan():
    print(n[0].decode('UTF-8'))



for connection in connections:
    station1, station2, password = connection.split()
    station = station1 + " " + station2
    print(station.encode('UTF-8'))
    station = "Moon" + b'\xe2\x80\x99'.decode('UTF-8')+"s House"

    print("Connecting to {}.".format(station))

    sta_if.connect(station, password)

    for i in range(15):
        print(".")
        if sta_if.status() == network.STAT_WRONG_PASSWORD:
            print("Wrong Password!")
        elif sta_if.status() == network.STAT_NO_AP_FOUND:
            print("No AP Found")
        elif sta_if.status() == network.STAT_CONNECTING:
            print("Connecting")
        else:
            print(sta_if.status())

        if sta_if.isconnected():
            break

        time.sleep(1)

    if sta_if.isconnected():
        break
    else:
        print("Connection could not be made.\n")


if sta_if.isconnected():
    print("Connected as: {}".format(sta_if.ifconfig()[0]))
