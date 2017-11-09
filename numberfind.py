from urllib import urlopen
one_digit = range(1, 9) #All possible combinations of 1 digit
two_digit = range(10, 99) #All possible combinations of 2 digits
three_digit = range(100, 999) #All possible combinations of 3 digits
four_digit = range (1000, 9999) #All possible combinations of 4 digits
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
