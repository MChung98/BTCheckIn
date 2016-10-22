import bluetooth
import time

print "In/Out Board"

home = False

while True:
  print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

  result = bluetooth.lookup_name('74:A5:28:EC:31:3C', timeout=5)
  if (result != None):
    print "Kevin: in"
    if(home == False):
        home = True
        ftp = ftplib.FTP("KevinAiken.com")
        ftp.login("KevinAiken@ashleighart.com", "MichaelChung1!")
        ftp.cwd('/kevinaiken')
        ftp.storbinary("STOR AmIHome.html", StringIO.StringIO('Kevin is home in'))
        ftp.quit()
  else:
    print "Kevin: out"
    if(home):
        home = False
        ftp = ftplib.FTP("KevinAiken.com")
        ftp.login("KevinAIken@ashleighart.com", "MichaelChung1!")
        ftp.cwd('/kevinaiken')
        ftp.storbinary("STOR AmIHome.html", StringIO.StringIO('Kevin is out'))
        ftp.quit()

  time.sleep(10)
