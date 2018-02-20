#!/usr/bin/python3

from time import sleep

def get(q):
	try:
		return input(q)
	except:
		return raw_input(q)

def execute(path):
	lvars = {}
	lints = {}
	with open(path) as f: raw = f.read()
	lines = raw.split("\n")
	cmdlist = []
	i = 0
	while i < len(lines):
		cmdlist.append(lines[i].split())
		i += 1
	i = 0
	while i < len(cmdlist):
		if cmdlist[i] == []:
			pass
		elif cmdlist[i][0] == 'echo' or cmdlist[i][0] == 'print':
			out = ""
			ii = 1
			while ii < len(cmdlist[i]):
				out = out + cmdlist[i][ii] + " "
				ii += 1
			print(out)
		elif cmdlist[i][0] == 'sleep' or cmdlist[i][0] == 'wait':
			sleep(int(cmdlist[i][1]))
		elif cmdlist[i][0] == 'raise':
			ii = 1
			err = ""
			while ii < len(cmdlist[i]):
				err = err + cmdlist[i][ii] + " "
				ii += 1
			exec("raise " + err)
		elif cmdlist[i][0] == 'var':
			vn = cmdlist[i][1]
			vv = ""
			ii = 2
			while ii < len(cmdlist[i]):
				vv = vv + cmdlist[i][ii] + " "
				ii += 1
			vv[:-1]
			lvars[vn] = vv
		elif cmdlist[i][0] == 'int':
			vn = cmdlist[i][1]
			vv = int(cmdlist[i][2])
			lints[vn] = vv
		elif cmdlist[i][0] == 'printvar' or cmdlist[i][0] == 'echovar':
			print(lvars[cmdlist[i][1]])
		elif cmdlist[i][0] == 'printint' or cmdlist[i][0] == 'echoint':
			print(lints[cmdlist[i][1]])
		else:
			raise ValueError("Unknown command")
		i += 1

if __name__ == "__main__":
	execute("filename")
