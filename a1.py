import random
def attack():	
	
	key1 = random.randint(0, 4294967295)
	key2 = random.randint(0, 4294967295)
	key3 = random.randint(0, 4294967295)
	key4 = random.randint(0, 4294967295)
	
	unKnown_key = [key1, key2, key3, key4]
	print unKnown_key
	
	L = [['00000000', '10110100', '00000000', '00000000'], \
         	['00000000', '01000101', '00000000', '00000000']]

	
	print("building 10,000 known pairs...")
   	known_pairs = generateKnownPairs(unknown_key, 10)
	





def generateKnownPairs(key,pair_count):
	 pairs = {}
	 for i in range(pair_count):
		knownPlaintext[i] = [randrange(2) for j in range(64)]
        		#knownCiphertext[i] = encrypt(knownPlaintext[i], key)
		#print (  knownPlaintext[i])
        		#print (  knownCiphertext[i])



attack()

	