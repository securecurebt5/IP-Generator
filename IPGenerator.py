#!/usr/bin/env python
# WebSite: http://www.pentestingskills.com/
# Author : Boumediene Kaddour
# Name   : IPGenerator.py
# Purpose: Generates IPs for a given network
# Country: Algeria
# Email  : snboumediene@gmail.com
try:
	from IPCalc import IPCalc
except:
	print "IPCalc.py doesn't exist"
	exit(1)

from sys import argv
if len(argv) != 2:
	print "Usage:\n\tpython %s IP/CIDR\n\ti.e. 172.16.122.10/25"%argv[0]
	exit(1)
cidr = argv[1]
addrs =IPCalc(cidr)
fst, last = addrs[3], addrs[4]
lst1 = []
lst2 = []
indxBool1 = False
indxBool2 = False
indx = 0

for i, j in zip(fst, last):
	if i == j:
		indx+=1
	else:
		if indx == 1:
			for octet in range(int(i), int(j)+1):
				indxBool1 = True
				lst1.append(octet)
			indx+=1
		elif indx == 2:
			for octet in range(int(i), int(j)+1):
				indxBool2 = True
				lst2.append(octet)
			indx+=1
		elif indx == 3:
			if indxBool1 is True:
				genindx = 1
			elif indxBool2 is True:
				genindx = 2
			else:
				genindx = indx
			if genindx == 1:
				for octet in lst1:
					for octet2 in lst2:
						for octet3 in range(int(i), int(j)+1):
							print ".".join( [ str(p) for p in fst[0:genindx ] ] )+".%s.%s.%s"%(octet, octet2, octet3)
			elif genindx == 2:
				for octet in lst2:
					for octet2 in range(int(i), int(j)+1):
						print ".".join( [ str(p) for p in fst[0:genindx] ] )+".%s.%s"%(octet, octet2)
			else:
				for octet in range(int(i), int(j)+1):
					print ".".join( [ str(p) for p in fst[0:genindx ] ] )+".%s"%octet
		else:	
			pass
