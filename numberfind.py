import sys
import getopt
import re
from urllib.request import urlopen
one_digit = range(0, 10) #All possible combinations of 1 digit  (range will be start from 0 and stop at 9 so use 10 as last number)
two_digit = range(0, 100) #All possible combinations of 2 digits
three_digit = range(0, 1000) #All possible combinations of 3 digits
four_digit = range (0, 10000) #All possible combinations of 4 digits
five_digit = range (0, 100000)
#six_digit = range (100000, 999999)
#seven_digit = range (1000000, 9999999)

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, "p:", ["n="]) #args #shortopts #longopts
#print(opts)

for opt, arg in opts:
	if opt == '-p':
		number = arg
	elif opt == '--n':
		name = arg
#print(type(number)) 
# print(args) 

num = []
nums = []
# num.append(number)
no = 10 - len(number)
 
while no:
	print ("\n[+] Geanerating sequences of number:")
	print ("------------------------------------\n")
	if no == 4:
		for n in four_digit:
			nums.append(number + str(n).zfill(no))
			#print(number + str(n).zfill(no))
		break
	elif no ==3:
		for n in three_digit:
			nums.append(number + str(n).zfill(no))
			#print (number + str(n).zfill(no))
		break
	elif no == 2:
		for n in two_digit:
			nums.append(number + str(n).zfill(no))
			#print(number + str(n).zfill(no))
		break
	elif no == 1:
		for n in one_digit:
			nums.append(number + str(n).zfill(no))
			#print(nums)
		break
	else:
		print('number not valid')
		break
else:
	print('\n', 'number should be less than 10 and grater than 5', '\n')

if nums:
	print ("\n[+] Writing number in file:")
	print ("------------------------------------\n")
	file_name = "numbers.txt"
	f = open(file_name, "w")
	header = "numbers found:\n"
	f.write(header)
	for s in nums:
		#td = sc.b
		#tw = sc.a["href"]
		f.write(" -" + s + "\n")
	print(' writed ')
	f.close()
for nomber in nums: #Checking a combination from the list of all possible combinations
	url = 'http://numberfinder.com/find.php?q=' + nomber + "&submit=ok" #Making a request to the phone lookup web service
	result = urlopen(url).read().lower() #Reading the response

	if 'googlebot' in str(result): #Checking if neha is in the response
		# print (nomber) #Prints the combination whose result has neha in it
		file_name = "web.txt"
		f = open(file_name, "a")
		header = "web found:\n"
		f.write(header)
		f.write(" -" + nomber + '\n')
		f.close()
	else:
		pass
		#print ("no", nomber)

"""
for n in range(no, 0, -1):
	#number += '0'
	num.append(n)
	print (num)
	#if len(number)
	#n = n+1
for i in num:
	print(i)
"""


















""" Old Version got Updated on 11/11/17
# Checking for 1 digit combination
for number in one_digit: #Checking a combination from the list of all possible combinations
	url = 'numberfinder.com/find.php?q=981241000' + number + "&submit=ok" #Making a request to the phone lookup web service
	result = urlopen(url).read().lower() #Reading the response
	if 'neha' in result: #Checking if neha is in the response
		print number #Prints the combination whose result has neha in it
	elif number = 9: #When we have reached the last 1 digit combination i.e. 9
		for number in two_digit:
			url = 'numberfinder.com/find.php?q=98124100' + number + "&submit=ok"
			result = urlopen(url).read().lower()
			if 'neha' in result:
				print number
			elif number = 99: #When we have reached the last 2 digit combination i.e. 99
				for number in three_digit:
					url = 'numberfinder.com/find.php?q=9812410' + number + "&submit=ok"	
					result = urlopen(url).read().lower()
					if 'neha' in result:
						print number
					elif number = 999: #When we have reached the last 3 digit combination i.e. 999
						for number in three_digit:
						url = 'numberfinder.com/find.php?q=981241' + number + "&submit=ok"	
						result = urlopen(url).read().lower()
						if 'neha' in result:
							print number
						elif number = 9999: #The last combination
							print "Bruteforce is over"
							quit()
						else:
							pass
					else:
						pass
			else:
				pass
	else:
		pass
"""