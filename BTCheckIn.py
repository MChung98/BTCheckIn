# import bluetooth
import time
import os.path
import MySQLdb
print "In/Out Board"

home = False

db = MySQLdb.connect("localhost","monitor","MichaelChung1!", "users")
cursor = db.cursor()
query = "SELECT * FROM usersdat"

cursor.execute(query)

results = cursor.fetchall()


print 'leo'
for row in results:
    print row

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
                    # send notification to server that aI'm in
                else:
                    print "Kevin: out"
                if(home):
                    home = False
                    # send notification to server that I'm out

        except:
            print("Errrroooooooeeer")
            break

time.sleep(10) # change to every few minutes for final
