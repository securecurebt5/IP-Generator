#!/usr/bin/env python
# WebSite: http://www.pentestingskills.com/
# Author : Boumediene Kaddour
# Name   : IPCalc.py
# Purpose: Calculates the IP Range of a given Network
# Country: Algeria
# Email  : snboumediene@gmail.com
class IPrange:
	def __init__(self, address, cidr):
		self.address = address
		self.cidr = cidr
		self.addrlist = self.address.split(".")

	def __repr__(self):
		print "Program started!"
		print "Calculation of IPRange for %s/%s has been successfully completed" % (self.address,self.cidr)

	def MASK(self):
		mask = [0,0,0,0]
		for i in range(int(self.cidr)):
			mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
		return mask

	def NETWORK(self):
		network = []
		for i in range(4):
			network.append(int(self.addrlist[i]) & self.MASK()[i])
		return network

	def REVERSE(self):
		mask = self.MASK()
		for i in range(4):
			mask[i] = ~ mask[i] & 0xFF
		return mask

	def BROADCAST(self):
		broadcast = []
		net = self.NETWORK()
		rev = self.REVERSE()
		for i in range(4):
			broadcast.append(int(net[i])  | int(rev[i]))
		return broadcast

	def FIRST_ADDR(self):
		b = self.BROADCAST()
		net = self.NETWORK()
		f = []
		for i in range(4):
			if net[i] == b[i]:
				f.append(net[i])
			else:
				b[i] = ~ b[i] & 0xFF
				if i == 3 :
					f.append(net[i]+1)
				else:
					f.append(net[i])
		return f

	def LAST_ADDR(self):
		last_from_broadcast = self.BROADCAST()
		last_from_broadcast[-1] = last_from_broadcast[-1] & 0xFE
		return last_from_broadcast

def IPCalc(IP_MASK):
	if "/" in IP_MASK:
		address, cidr = IP_MASK.split("/")
		obj = IPrange(address, cidr)
		obj.__repr__()
		NETWORK  = ".".join( [ str(octet) for octet in obj.NETWORK()])
		MASK     = ".".join( [ str(octet) for octet in obj.MASK()])
		BROADCAST=".".join( [ str(octet) for octet in obj.BROADCAST()])
		FIRST_IP =  obj.FIRST_ADDR()
		LAST_IP  = obj.LAST_ADDR()
		return NETWORK,MASK,BROADCAST,FIRST_IP, LAST_IP
	else:
		print "Please, Specify a valid CIDR Network -- 172.16.122.2/22"
	
