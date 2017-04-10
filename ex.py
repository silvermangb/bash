import subprocess

proc = subprocess.Popen(['./bash','-c','`ls`'])
proc.wait()
