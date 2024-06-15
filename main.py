from subprocess import Popen

if Popen('sc query "AntiCheatExpert Service" | find /c "START"')>0:
  Popen('sc stop "AntiCheatExpert Service"')
