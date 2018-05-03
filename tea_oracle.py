from ctypes import *
from sys import *
import time
import random
PBox=[0,16,32,48,1,17,33,49,2,18,34,50,3,19,35,51,4,20,36,52,5,21,37,53,6,22,38,54,7,23,39,55,8,24,40,56,9,25,41,57,10,26,42,58,11,27,43,59,12,28,44,60,13,29,45,61,14,30,46,62,15,31,47,63]

Sbox = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]

def sBoxLayer(state):
    	output = 0
    	for i in xrange(16):
        	output += Sbox[( state >> (i * 4)) & 0xF] << (i * 4)
    	return output

def pLayer(state):    
    	output = 0
    	for i in xrange(64):
        	output += ((state >> i) & 1) << PBox[i]
    	return output

def encrypt(block, passedkey):	
	sidea=block1
	sideb=block2
	sum=0
	delta=0x9E3779B9
	returnblock=[0,0]
	sum += delta
	sidea= (( sideb<< 4 ) + passedkey[0]) ^ (sideb + sum) ^ (( sideb >> 5 ) + passedkey[1])
	sidea  = sBoxLayer(sidea)
	sideb  = pLayer(sideb)		
	returnblock[0]=sidea
	returnblock[1]=sideb
	return returnblock
	
if (len(argv) != 2):
	print ("Usage: python tea_oracle.py <name_of_output_file>")
	exit(1)
key1 = random.randint(0, 4294967295)
key2 = random.randint(0, 4294967295)
key3 = random.randint(0, 4294967295)
key4 = random.randint(0, 4294967295)
key = [key1, key2, key3, key4]
print "Random key: %0.8x %0.8x %0.8x %0.8x" % (key1, key2, key3, key4)
f = open(argv[1], 'w')
for i in range (25):
	block1 = random.randint(0, 4294967295)
	block2 = random.randint(0, 4294967295)
	f.write("%0.8x %0.8x, " % (block1, block2))
	msg = [block1, block2]
	encrypted = encrypt(msg, key)
	f.write("%0.8x %0.8x\n" % (encrypted[1], encrypted[0]))
print "Printed 100 plaintext/ciphertext pairs to " + argv[1] + " using above key"