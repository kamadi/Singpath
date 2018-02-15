#136.List Head
def head(list):
	return list[0]

print("136:",head([1,2,3]))

#137.List Head & Tail
def ends(list):
	return [list[0],list[len(list)-1]]

print("137:",ends([1,2,3,4]))

#138.Remove Item
def remove(l,item):
	return list(filter(lambda a: a != item, l))
	
print("138:",remove([1,2,3,3,4,3],3))

#139.Reverse a list
def reverse_list(l):
	return l[::-1]
	
print("139:",reverse_list([1,2,3,4]))
	
#140.List Contains
def list_contains(l):
	return list(set(l))

print("140:",list_contains([1,2,3,3,4,3]))

#141.Check whether a list is palindrome
def check_palin(l):
	return l == l[::-1]

print("141:",check_palin([1,2,3,3,2,1]))

#142.Parse String
def words(s):
	return s.split()
	
print("141:",words("This is a sentence"))

#143.Drop every N'th element from a list
def drop(l,step):
	for i in range(step,len(l),step):
		l.pop(i)
	return l

print("143:",drop(['h','e','l','l','o'],3))

#144.Sorting a list
def sort(l):
	l.sort()
	return l

print("144:",sort([9,2,6,3,4,3]))

#145.Is Sorted
def is_sorted(l):
	return sorted(l) == l

print("145:",is_sorted([1,2,3,3,4,5]))

#146.Has Duplicates
def has_duplicates(l):
	return len(set(l)) != len(l)
	
print("146:",has_duplicates([1,2,3,3,4,5]))

#147.String Length Histogram
def word_length_list(s):
	l = s.split()
	res = []
	for item in l:
		res.append(len(item))
	return res

print("147:",word_length_list("a bb ccc dddd eeeee"))

#148.Building a String
def buildString(l,s):
	return s.join(str(e) for e in l)

print("148:",buildString([4,5,3],'hi'))	

#149.Range
def list_range(l):
	min = l[0]
	max = l[0]
	for item in l:
		if item > max:
			max = item
		if item < min:
			min = item
	return max-min
	
print("149:",list_range([10, 3, 5, 6]))

#150.Centered Average
def centered_average(l):
	max = l[0]
	min = l[0]
	sum = 0
	for item in l:
		if item > max:
			max = item
		if item < min:
			min = item
		sum += item

	return (sum - max - min) / (len(l) - 2)
	
print("150:",centered_average([1, 2, 3, 4, 100]))

#151.Has 22
def has22(l):
	is_found = False
	for item in l:
		if item == 2:
			if is_found:
				return True
			is_found = True
		else:
			is_found = False
			
	return False
	
print("151:",has22([2,3,2, 2]))

#152.Sorting a List by String Length
def sort_by_length(l):
	return sorted(l,key=lambda item:len(str(item)),reverse = True)
	
print("152:",sort_by_length([46, ['meh', 3], 'Hahahaha', {'yi':'one', 'er':'two', 'san':'three'}, 'test']))

#153.Sort List Based on Two Criteria
def sortlist(l):
	return sorted(l,key=lambda item: (-len(item), item))
	
print("153:",sortlist(['cba','dca','ccc','bb','a']))

#154.Frequency
def frequency(l,n):
	count = 0
	for item in l:
		if item == n:
			count+=1
	return count
	
print("154:",frequency([1,2,3,4],2))

#154.Deep Sort
def deepsort(lists):
	res = []
	for list in lists:
		res+=set(list)
	return sorted(set(res),key = lambda item: len(str(item)))
	
print("155:",deepsort([['aa','cc','ab'],[1,3,2]]))

#156.Word Split
def word_split(s):
	return list(s.replace(" ", ""))

print("156:",word_split("word to split"))

#157.Most Common Item
def mostCommonItem(l):
	return max(set(l), key=l.count)
	
print("157:",mostCommonItem([3,6,5,5,8,5,2,3]))

#158.Statistical Distribution Skewness
def stats_skew(l):
	sortedList = sorted(l)
	n = len(l)
	median = None
	index = (n - 1) // 2
	if n % 2 == 1:
		median = sorted(l)[index]
	else:
		median = (sortedList[index] + sortedList[index + 1])/2.0
		
	mean = sum(l) / n
	if mean > median:
		return "positively skewed"
	if median > mean:
		return "negatively skewed"
	return "normal"
	
print("158",stats_skew([1,41,39,40,55]))

