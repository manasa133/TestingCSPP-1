def sum0fDigits(n):
	sum=0
	while n:
		sum += n%10
		n//=10
	return sum

print (max([300,456,12345],key = sum0fDigits) )