from sty import fg, bg, ef, rs
import os
from faker import Faker
import requests
from threading import Thread

#Warning
print("This script is Windows only, dont execute on Linux/OSX")
input("Press any key to continue...")

#Ui
os.system("cls")
os.system("title reaper")
print(fg(118, 209, 0))
print ("""
                ...                            
              ;::::;                          
            ;::::; :;                          
          ;:::::'   :;                        
         ;:::::;     ;.                        
        ,:::::'       ;           OOO\        
        ::::::;       ;          OOOOO\        
        ;:::::;       ;         OOOOOOOO      
      ,;::::::;     ;'         / OOOOOOO      
     ;:::::::::`. ,,,;.        /  / DOOOOOO    
   .';:::::::::::::::::;,     /  /     DOOOO  
  ,::::::;::::::;;;;::::;,   /  /        DOOO  
 ;`::::::`'::::::;;;::::: ,#/  /          DOOO
 :`:::::::`;::::::;;::: ;::#  /            DOOO
 ::`:::::::`;:::::::: ;::::# /              DOO
 `:`:::::::`;:::::: ;::::::#/               DOO
  :::`:::::::`;; ;:::::::::##                OO
  ::::`:::::::`;::::::::;:::#                O
  `:::::`::::::::::::;'`:;::#                
   `:::::`::::::::;' /  / `:#        reaper
    ::::::`:::::;'  /  /   `#     Made by vanta            
                        
      1 - Check for Panels
      2 - Check for Websites""")
print(fg(41, 41, 41))

#I'm using faker to generate a random IPv4
def genIP():  
    faker = Faker()  
    IP = faker.ipv4() 
    return IP 

#Checks if the IP is online
def checkIP():
    while True:
        IP = genIP()
        try:
            req = requests.get("http://" + IP)
            checkPanel(IP)
        except:
            print(fg(163, 59, 60) + IP)
    
#Checks if the IP has a Login Panel   
def checkPanel(IP):
    with open('Panel_Links.txt') as f:
        for line in f.read().splitlines():
            try:
                req = requests.get("http://" + IP + line)
                if req.status_code == 200:
                    print(fg(118, 209, 0) + IP + line)
            except:
                pass

#Checks if the IP is online
def checkIPWeb():
    while True:
        IP = genIP()
        try:
            req = requests.get("http://" + IP)
            checkWeb(IP)
        except:
            print(fg(163, 59, 60) + IP)

#Checks if the IP is a website   
def checkWeb(IP):
    with open('Dont_Touch_Cuz_im_Lazy.txt') as f:
        for line in f.read().splitlines():
            try:
                req = requests.get("http://" + IP + line)
                if req.status_code == 200:
                    print(fg(118, 209, 0) + IP + line)
            except:
                pass

#Does what number 1 does
num = input("Choose a number: ")
if num == "1":
    threadcount = int(input("How many threads: "))
    os.system("cls")
    #I know this code below looks like trash
    print(fg(118, 209, 0) + "Green IP = Valid" + fg(255, 255, 255) + " | " + fg(163, 59, 60) + "Red IP = Invalid")
    for i in range(threadcount):
        thread = Thread(target=checkIP)
        thread.start()
    checkIP()
    
#Does what number 2 does
elif num == "2":
    threadcount = int(input("How many threads: "))
    os.system("cls")
    #I know this code below looks like trash
    print(fg(118, 209, 0) + "Green IP = Valid" + fg(255, 255, 255) + " | " + fg(163, 59, 60) + "Red IP = Invalid")
    for i in range(threadcount):
        thread = Thread(target=checkIPWeb)
        thread.start()
    checkIP()

#Exits if the input isnt a number
elif num.isdigit() == False:
  exit()
#Exits if the input isnt 1 or 2
else:
  exit()






