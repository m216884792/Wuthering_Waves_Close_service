
import os
from mod.groceries import strPopen,nonstrPopen
from time import sleep
from mod.Wurthering_Wave_Close_service import checkth


exename ='KRInstallExternal.exe'

check=checkth(5)
check.start()

nonstrPopen(f'{os.getcwd()}/launcher.exe')

while True:
  sleep(10)
  if len(strPopen(f'tasklist | find "{exename}"'))<10:
    break

check.stop()

