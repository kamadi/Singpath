# 79.While Loop
def sum(max):
    i = 1
    sum = 0
    while i <= max:
        sum += i
        i += 1
    return sum


print ("79:", sum(3))


# 80.Sum range
def sum_of_range(start, end):
    sum = 0
    while start <= end:
        sum += start
        start += 1
    return sum


print ("80:", sum_of_range(-23, -4))


# 81.Sum range by Step
def sum_of_range(start, end, step):
    sum = 0
    while start <= end:
        sum += start
        start += step
    return sum


print ("81:", sum_of_range(-2, 100, 5))

#82. For Loops
def sum_by_range(n):
	sum = 0
	for i in range(n+1):
		sum += i * i
	return sum

print("82:", sum_by_range(3))


#83. Square Roots

import math

def sum_roots(n):
	sum = 0
	for i in  range(1,n+1):
		sum += math.sqrt(i)
	return sum

print("83:",sum_roots(3))


#84. Cubes
def sum_of_cubes(a,b):
	sum = 0
	for i in range(a,b+1):
		sum += math.pow(i,3)
	return sum

print("84:",sum_of_cubes(-23,-4))
	
#85. Sum Powers Over Range
def sum_of_number_by_power(a,b,power):
	sum = 0
	for i in range(a,b+1):
		sum+=math.pow(i,power)
	return sum

print("85:", sum_of_number_by_power(12,150,6))

#86. Product of range
def product_of_range(a,b,step):
	sum = 1
	for i in range(a,b+1,step):
		sum *= i
	return sum

print("86:", product_of_range(12,150,6))

#87. Iteration - Sum of the squares of a list of numbers
def sum_of_square_in_list(list):
	sum = 0
	for i in list:
		sum += i*i
	return sum

print("87:",sum_of_square_in_list([1,6,7.3,9,2,4,6]))

#88. Count Evens
def count_evens(list):
	count = 0
	for i in list:
		if i % 2 == 0:
			count+=1
	return count

print("88:",count_evens([2, 1, 2, 3, 4]))

#89. sum67
def sum67(list):
	sum = 0
	size = len(list)
	i = 0
	while i < size:
		if list[i] == 6:
			j = i + 1
			while list[j] != 7:
				j+=1
			i = j
		else:
			sum+=list[i]
		i+=1
	return sum

print("89:", sum67([6, 7, 11]))

#90. Duplicate the elements in a list
def duplicate_element_list(list):
	arr = []
	for i in list:
		arr.append(i)
		arr.append(i)
	return arr

print(duplicate_element_list([1,2]))

#91.Prime Numbers
def is_prime(n):
	if n == 0 or n == 3:
		return True
		
	if n%2 == 0 or n%3 ==0:
		return False
	
	i = 5
	
	w = 2

	while i * i <= n:
		if n % i == 0:
			return False

		i += w
		w = 6 - w

	return True

print("90:",is_prime(947))

#92.Adding all natural numbers
def add_all_natural_numbers(n):
	sum = 0
	for i in  range(5,n+1):
		if i%5 == 0 or i%7 == 0:
			sum+=i
	return sum

print("92:",add_all_natural_numbers(50))

#93.Perfect Numbers
def is_perfect(n):
	i = 1
	sum = 0
	while i<=n/2:
		if n%i == 0:
			sum+=i
		i+=1
	return sum == n	

print("93:",is_perfect(496))

#94.A list of prime numbers
def list_of_prime_numbers(n):
	list = []
	for i in range(1,n+1):
		if is_prime(i):
			list.append(i)
	return list

print("94:",list_of_prime_numbers(100))

#95.Count to Number
def count_to_number(n):
	s = ""
	for i in range(1,n+1):
		s+=str(i)
	return s
	
print("95:",count_to_number(10))

#96.Symmetric Number Judge
def is_symmetric(n):
	return str(n) == str(n)[::-1]

print("96:",is_symmetric(21566512))

#97.Count the number of Prime Numbers
def count_prime_numbers(n):
	count = 0
	for i in range(1,n+1):
		if is_prime(i):
			count+=1
	return count

print("97:",count_prime_numbers(100))

	
		
		
