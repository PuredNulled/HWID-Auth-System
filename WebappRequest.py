import requests, subprocess, colorama

from colorama import Fore

colorama.init()

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

def Auth():
    r = requests.get(f'http://localhost:8080/backend?hwid={hwid}')
    if r.status_code == 401:
        return False
    if r.status_code == 200:
        return True

if __name__ == '__main__':
    isAuth = Auth()
    if isAuth == False:
        print("You're not whitelisted")
        print()
        print("HWID: "+Fore.YELLOW+hwid)
    if isAuth == True:
        print("You're whitelisted")
