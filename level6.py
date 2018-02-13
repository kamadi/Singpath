#102.Strings
def character(s,n):
	return s[n]
	
print("102:",character("123456789",3))

#103.Hello
def hello(s):
	return "Hello "+s+"!"

print("103:",hello("Madi"))

#104.String Slice
def middle(s):
	return s[1:len(s)-1]

print("104:",middle("Mississippi"))

#105.String Search
def search_char(s,s1):
	i = 0
	while i<len(s):
		if s[i] == s1:
			return i
		i+=1	
	return -1
	
print("105:",search_char("blob","l"))

#106.Search Upgrade
def search_word(s,word):
	return s.find(word)
	
print("106:",search_word('478294','8294'))

#107.Upper Case
def upper_case(s):
	return s.upper()

print("107:",upper_case("fRiend"))

#108.Strip Last 3
def strip_last_3(s):
	return s[:-3]
	
print("108:",strip_last_3("hello!"))

#109.Change Case
def change(s):
	return s.swapcase()
	
print("109:",change("HellO"))

#110.String Reversal
def reverse(s):
	return s[::-1]
	
print("110:",reverse("hello"))

#111.Debugging Strings
def is_reverse(s1,s2):
	return s1 == s2[::-1]

print("111:",is_reverse("hello","olleh"))

#112.Make Tags
def make_tag(tag,s):
	return "<"+tag+">"+s+"<"+tag+"/>"

print("112:",make_tag("p","text"))

#113.Ends With
def end_with(s1,s2):
	l1 = len(s1)
	l2 = len(s2)
	if l1>l2:
		return s1.lower()[l1-l2:l1] == s2.lower()
	return s2.lower()[l2-l1:l2] == s1.lower()

print("113:",end_with('HiaBc', 'iAdBc'))

#114.Concatenate strings
def concatenate(list,delim=' '):
	return delim.join(list)

print("114:",concatenate(['To', 'seek', 'the', 'Holy', 'Grail'],","))

#115.Find xyz
def xyz_there(s):
	i = s.find("xyz")
	if i == 0:
		return True
	if i > 0 and s[i-1] != '.':
		return True
	if i > 0 and s[i-1] == '.' and i+3 <len(s) and s[i+3] == '.':
		return True
	return False

print("115:",xyz_there('.xyz.xyz2xyz'))

#116.Comparing Strings
def in_both(s1,s2):
	return ''.join(sorted(set(s1.lower()).intersection(set(s2.lower()))))

print("116:",in_both("apple","pie"))

#117.Echo
def echo(s):
	return s+s[len(s)-2:len(s)]*4

print("117:",echo("Hello"))

#118.Is Anagram
def is_anagram(s1,s2):
	return sorted(s1) == sorted(s2)

print("118",is_anagram("banana","ananab"))

#119.Interlock
def interlock(s1,s2):
	list1 = list(s1)
	list2 = list(s2)
	len1 = len(list1)
	len2 = len(list2)
	result = ""
	if len1 > len2:
		for i in range(len1):
			result+=list1[i]
			if i < len2:
				result+=list2[i]
	elif len2 > len1:
		for i in range(len2):
			result+=list2[i]
			if i < len1:
				result+=list1[i]
	else:
		for i in range(len1):
			result+=list1[i]
			result+=list2[i]
	return result

print("119:",interlock("abalone","hammer"))

#120.Sandwich
def combo_string(s1,s2):
	if len(s1) > len(s2):
		return s2+s1+s2
	return s1+s2+s1
	
print("120:",combo_string("hello","hi"))

#121.Half String
def half(s,is_front = True):
	if is_front:
		return s[0:int(len(s)/2)]
	return s[int(len(s)/2):len(s)]

print("120:",half("Hiho",False))

#122.Parse a string
def parse(s):
	return s.replace("'"," ").replace("."," ").replace(","," ").split()
	
print("122:",parse("Listen, strange women lyin' in ponds distributin' swords is no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony."))

#123.Lucky Number
def lucky_number(s):
	list = s.split()
	return (2*len(list[0])*len(list[1]))%10
	
print("123:",lucky_number("David Crane"))




		
			
			