from time import sleep
from .groceries import strPopen

def checkth(sleeptime:int):
  exename ='Wuthering Waves.exe'
  exename2 = 'AntiCheatExpert Service'
  while True:
    sleep(sleeptime)
    if len(strPopen(f'tasklist | find "{exename}"'))>10: #有無運行
        if int(strPopen(f'sc query "{exename2}" | find /c "STATE"'))>0:  #服務狀態
          strPopen(f'sc stop "{exename2}"')  #關閉服務
