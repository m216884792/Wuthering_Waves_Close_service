import os
from mod.groceries import strPopen
from time import sleep
from mod.Wurthering_Wave_Close_service import checkth
from threading import Thread


exename ='KRInstallExternal.exe'

Thread(target=checkth,args=[5]).start()

strPopen(f'{os.getcwd()}/launcher.exe')

while len(strPopen(f'tasklist | find "{exename}"'))>10:
  sleep(10)

os._exit(1)

