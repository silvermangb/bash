import sys
import subprocess

bash = ['./bash','bash']

params = r"'a' '';sleep 20''"

cmd = 'echo'

cmd_line = cmd +' ' + params

proc = subprocess.Popen([bash[0],'-c',cmd_line])
proc.wait()

