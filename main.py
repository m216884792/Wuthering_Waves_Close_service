from subprocess import Popen,check_output,run
from time import sleep
import configparser


if int(run(sc query "Wurthering_Wave_Close_service" | find /c "FAILED", shell=True, capture_output=True, text=True))!=0: #沒有服務
  run(f'sc create "Wurthering_Wave_Close_service" binpath = "{os.getcwd()}/main.exe" start= auto displayname = "鳴潮自動停止ACE服務"', shell=True) #創建服務
  run('sc start "Wurthering_Wave_Close_service"', shell=True) #啟動服務

while True:
  sleep(5)
  if len(run(f'tasklist | find "Wuthering Waves.exe"', shell=True, capture_output=True, text=True))>10: #有無運行
    if int(run('sc query "AntiCheatExpert Service" | find /c "START"', shell=True, capture_output=True, text=True))>0:  #服務狀態
      run('sc stop "AntiCheatExpert Service"', shell=True)  #關閉服務





run(wmic process where name="SGuard64.exe" CALL setpriority "idle", shell=True)
run(wmic process where name="SGuardSvc64.exe" CALL setpriority "idle", shell=True)
