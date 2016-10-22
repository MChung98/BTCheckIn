import bluetooth
import time

print "In/Out Board"

while True:
  print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

  result = bluetooth.lookup_name('74:A5:28:EC:31:3C', timeout=5)
  if (result != None):
    print "Kevin: in"
  else:
    print "Kevin: out"

  time.sleep(10)
  
