import bluetooth
import time
import os.path
import MySQLdb

print "In/Out Board"

home = False

db = MySQLdb.connect("localhost","monitor","MichaelChung1!", "users")
cursor = db.cursor()

while True:
    if((os.path.isfile(users.txt)) == False):
        file = open('users.txt', rw)
    while True:
        try:
            currentID = file.readline()
            print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
            result = bluetooth.lookup_name(currentID, timeout=5)
            if (result != None):
                sql = "INSERT INTO usersdat VALUES (%s,%s,%s,%s) / ("+ currentID + "," + result + "," + time.gmtime() + "," + time.gmtime() + ")"

                cursor.execute(sql)
                db.commit()
                print result + ": in"
                if(home == False):
                    home = True
                    # send notification to server that a I'm in
                else:
                    print result + ": out"
                if(home):
                    home = False
                    # send notification to server that I'm out
        except:
            print("Errrroooooooeeer")
            break

db.close()
time.sleep(10) # change to every few minutes for demo
