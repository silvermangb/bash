#!/usr/bin/env python

import sys
import subprocess
import datetime

def test(cmd):
	print 'command:',' '.join(cmd)
	sys.stdout.flush()
	sleep_command_present = cmd[-1].find('sleep')!=-1
        if sleep_command_present:
		start_time = datetime.datetime.now()
	proc = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	proc.wait()
	stdout,stderr = proc.communicate()
	print stdout
	print stderr
	if sleep_command_present:
		stop_time = datetime.datetime.now()
		print 'time delta: ', stop_time-start_time

tests_cases = open(sys.argv[1],'r')
i = 1
for line in tests_cases:
	print '----\ntest case '+str(i)
	tokens = line.strip().split(' ')
	cmd = ' '.join(tokens[1:])
	print '--'
	tokens = [None,tokens[0],cmd]
	tokens[0] = '/bin/bash'
	test(tokens)
	print '--'
	tokens[0] = './bash'
	test(tokens)
	i += 1
