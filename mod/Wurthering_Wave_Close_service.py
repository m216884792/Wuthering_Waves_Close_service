
from time import sleep
from .groceries import strPopen
from threading import Thread


class checkth():

  def __init__(self,sleeptime:int):
    self.sleeptime=sleeptime
    self.breakcl=False
    self.startth=Thread(target=self.th)

  def th(self):
    exename ='Wuthering Waves.exe'
    exename2 = 'AntiCheatExpert Service'
    while True:
      sleep(self.sleeptime)
      if len(strPopen(f'tasklist | find "{exename}"'))>10: #有無運行
          if int(strPopen(f'sc query "{exename2}" | find /c "STATE"'))>0:  #服務狀態
            strPopen(f'sc stop "{exename2}"')  #關閉服務

      if self.breakcl:
        break

  def start(self):
    if not self.startth.is_alive():
      self.startth=Thread(target=self.th)
      self.startth.start()

  def stop(self):
    self.breakcl=True
