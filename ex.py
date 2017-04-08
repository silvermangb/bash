import sys
import subprocess

bash = ['./bash','bash']

params = "a ';sleep 20'"
params = "'" + params + "'"

cmd = 'echo'

cmd_line = cmd +' ' + params

proc = subprocess.Popen([bash[0],'-c',cmd_line])
proc.wait()

