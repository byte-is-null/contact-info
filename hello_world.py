import itertools

#randomly numbers
x = [150,145,154,154,157,40,167,157,162,154,144]

#decrypto
for a,b,c in itertools.product(itertools.count(0),xrange(0,10),xrange(0,10)):
	print a,b,c

	#20ms delay between each character??
	if a > 20: break
