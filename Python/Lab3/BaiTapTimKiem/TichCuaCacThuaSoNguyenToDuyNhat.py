def productPrimeFactors(n):
	product = 1
	for i in range(2, n+1):
		if (n % i == 0):
			isPrime = 1
			for j in range(2, int(i/2 + 1)):
				if (i % j == 0):
					isPrime = 0
					break
			# điều kiện nếu \'i\' là số nguyên tố
            # cũng như hệ số của num
			if (isPrime):
				product = product * i
	return product
# main()
n = 44
print(productPrimeFactors(n))

