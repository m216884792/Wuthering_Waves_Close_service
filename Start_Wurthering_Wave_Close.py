import os
from mod.groceries import strPopen,nonstrPopen
from time import sleep


servicename = 'Wurthering_Wave_Close_service'
exename ='KRInstallExternal.exe'

if len(strPopen(f'tasklist | find "{servicename}"'))<10: #有無運行
  nonstrPopen(f'{os.getcwd()}/{servicename}.exe')

strPopen(f'{os.getcwd()}/launcher.exe')

while len(strPopen(f'tasklist | find "{exename}"'))>10:
  sleep(10)

