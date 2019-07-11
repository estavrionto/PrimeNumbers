#######################Brute Force Prime Number##########################
#by esta and muttaqi
#
#########################################################################

import time
a = time.time()

for i in range(1,1000):
	NotPrime = False
	for j in range(2,i):
		# print(i,j)
		if i%j ==0:
			NotPrime = True
			break
	if NotPrime != True:
		print('Prime Found :',i)
	b = time.time()
	# print("time ",b-a)

print(time.time() -a)
