from subprocess import Popen,check_output


if Popen(sc query "AntiCheatExpert Service" | find /c "FAILED")!=0:
  sc create "Wurthering_Wave_Close_service" binpath = "{os.getcwd()}/main.exe" start= auto displayname = "鳴潮自動停止ACE服務"
  sc start "Wurthering_Wave_Close_service"

check_output(f'tasklist | find "Wuthering Waves.exe"', shell=True)
if Popen('sc query "AntiCheatExpert Service" | find /c "START"')>0:
  Popen('sc stop "AntiCheatExpert Service"')
