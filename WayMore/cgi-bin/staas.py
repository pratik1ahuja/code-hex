#!/usr/bin/python2

import os
import cgi
import commands

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()

drive_name=data.getvalue("dn")
drive_size=data.getvalue("ds")

st_name=commands.getoutput('ls /media')

check=st_name.split('\n')

if drive_name in check:
	print "soory Drive already exist"
	print "<a href='http://192.168.10.113/stass.html'>"
	print "click here to go back"
	print "</a>"
else:
	#print commands.getoutput('sudo date')
	commands.getoutput('sudo lvcreate --name '+drive_name+' -V'+drive_size+'GB --thin new/p')

	commands.getoutput('sudo mkfs.xfs /dev/new/'+drive_name)

	commands.getoutput('sudo useradd -d /media/'+drive_name+' '+drive_name)

	commands.getoutput('sudo echo '+drive_name+' | sudo passwd '+drive_name+' --stdin')

	commands.getoutput('sudo mount /dev/new/'+drive_name+' /media/'+drive_name)

	redirectURL=  "http://192.168.10.113/welstass.html"
	print ('<html>')
	print ('<head>')
	print ('<meta http-equiv="refresh" content="0; url= '+str(redirectURL)+'" />')
	print ('</head>')
	print ('</html>')
	#print "sucess"
