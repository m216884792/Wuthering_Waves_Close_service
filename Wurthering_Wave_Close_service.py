from time import sleep
from mod.groceries import strPopen


exename ='Wuthering Waves.exe'

while True:
  sleep(10)
  if len(strPopen(f'tasklist | find "{exename}"'))>10: #有無運行
      if int(strPopen('sc query "AntiCheatExpert Service" | find /c "STATE"'))>0:  #服務狀態
        strPopen('sc stop "AntiCheatExpert Service"')  #關閉服務