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
