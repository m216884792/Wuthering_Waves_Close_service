from subprocess import Popen,check_output
from time import sleep


if Popen(sc query "AntiCheatExpert Service" | find /c "FAILED")!=0: #沒有服務
  Popen(f'sc create "Wurthering_Wave_Close_service" binpath = "{os.getcwd()}/main.exe" start= auto displayname = "鳴潮自動停止ACE服務"') #創建服務
  Popen('sc start "Wurthering_Wave_Close_service"') #啟動服務

while True:
  sleep((5)
  if len(check_output(f'tasklist | find "Wuthering Waves.exe"', shell=True))>0: #有無運行
    if int(Popen('sc query "AntiCheatExpert Service" | find /c "START"'))>0:  #服務狀態
      Popen('sc stop "AntiCheatExpert Service"')  #關閉服務
