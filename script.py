#!/usr/bin/python
import requests as r, os, threading
from threading import Thread
from colorama import Fore,Style
import time

print("""
________ ________ _______ ____  ____  ________ ________________ 
___  __ \___  __ \__  __ \__  |/ /_ \/ /___  / ____  _/___  __ )
__  /_/ /__  /_/ /_  / / /__    / __  / __  /   __  /  __  __  |
_  ____/ _  _, _/ / /_/ / _    |  _  /  _  /_____/ /   _  /_/ / 
/_/      /_/ |_|  \____/  /_/|_|  /_/   /_____//___/   /_____/  
TG Channel: @blackhat_lab | IDEA: @FS88ch
""")

time.sleep(5)

def clear():
	os.system('cls' if os.name=='nt' else 'clear')

def check(ip, prox):
	try:
		ipx = r.get("http://fsystem88.ru/ip", proxies={'http':'http://{}'.format(prox), 'https':'http://{}'.format(prox)}, verify=False, timeout=10).text
	except:
		ipx = ip
	if ip != ipx:
		print(Fore.GREEN+"{} good!".format(prox))
		f = open("proxies.txt", "a+")
		f.write("{}\n".format(prox))
		f.close()
	else:
		#print(Fore.RED+"{} bad".format(prox))
		pass

url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http"
req = r.get(url)
ip = r.post("http://fsystem88.ru/ip").text
array = req.text.split()
clear()
print(Fore.LIGHTYELLOW_EX+"Your ip: {}".format(ip)+Style.RESET_ALL)
open("proxies.txt", "w+").close()
for prox in array:
	thread_list = []
	t = threading.Thread (target=check, args=(ip, prox))
	thread_list.append(t)
	t.start()
