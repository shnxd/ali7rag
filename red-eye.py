import urllib.request
import sys
import socket
choose = True
ip = "x"
code = "y"
inp=input("x for ip and y for code: ")
if inp == ip :
	choose =False
elif inp == code :
	choose = True
else:
	print ("x for ip and y for coding")
if choose == True:
	ex="for example: http://google.com/"
	print (ex)
	response = urllib.request.urlopen(input("the link:"))
	html = response.read()
	print (html)
	
if choose == False :
	name=input('put the host:')
	ip=socket.gethostbyname(name)
	print('ip =',ip)