import socket
import requests
import json
import pprint
from colorama import init, Fore, Style

print(Fore.RED + """
    	░█▀▄░█▀█░█▀█░█▀▀░█▀▀░░░░░▀█▀░█▀█
        ░█▀▄░█▀█░█░█░█░█░▀▀█░▄▄▄░░█░░█▀▀
        ░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░░░░░▀▀▀░▀░░""")

host = input(Fore.BLUE + "\n Enter a domain name: ")
ip = socket.gethostbyname(host)
print(" ======================\n Geolocation:")
if not host:
        print(Fore.RED + "\n==================\nBruh -_-' Enter a domain Bro!")
        print(Fore.RED + "==================\n")

request = 'https://geolocation-db.com/jsonp/' + ip
response = requests.get(request)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)

for k,v in geolocation.items():
    
    pprint.pprint(str(k) + ' : ' + str(v))

print(Fore.GREEN + f"\nSo, the IP Address of the website is {ip}")
print("Maybe you want to try scanning with Nmap" + Fore.WHITE)
