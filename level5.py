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
