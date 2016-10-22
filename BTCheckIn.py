import bluetooth
import time
import os.path

print "In/Out Board"

home = False

while True:
    if((os.path.isfile(users.txt)) == False):
        file = open('users.txt', rw)
    while True:
        try:
            currentID = file.readline()
            print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
            result = bluetooth.lookup_name(currentID, timeout=5)
            if (result != None):
                print "Kevin: in"
                if(home == False):
                    home = True
                    # send notification to server
                else:
                    print "Kevin: out"
                if(home):
                    home = False
                    # send notification to server

        except:
            print("Errrroooooooeeer")
            break

time.sleep(10) # change to every few minutes for final
