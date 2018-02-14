#171.Dictionaries
question = {"color":"blue",7:"seven",3.14:[3,1,4,6]}

print("171:",question)

#172.List the keys of a dictionary
def sortedList(d):
	return sorted(list(d.keys()))

print("172:",sortedList({'a':1, 'c':2, 'b':3}))


#173.Reverse Lookup
def lookup(d,val):
    res = []
    for key,value in d.items():
        if value == val:
            res.append(key)
    return res

print("173:",lookup({'ta':4,8:'32',(5,3):'hi',(4,3,2):[4,3],'':4,73:8,839:234,34:857,'Hello':4},4))


#174.String Histogram
def histogram(s):
	l = s.split()
	res = {}
	for item in l:
		for c in item:
			if c in res:
				res[c] = res[c] + 1
			else:
				res[c] = 1
	return res
	
print("174:",histogram("a bb ccc dddd eeee"))

#175.List to Dictionary
def create_dict(l):
	res = {}
	for item in l:
		res[item] = item
	return res

print("175:",create_dict(['hi',7.8,34,'bye']))

#176.Switch Keys and Values
def switch(d):
	new_dic = {}
	for key,value in d.items():
		new_dic[value] = key
	return new_dic
	
print("176:",switch({"one":1,"two":2,"three":3,"four":4,"five":5}))

#177.String Building
def string(d):
	s = ""
	for key,value in d.items():
		s+=str(key)+"="+str(value)+";"
	return s[:-1]
	
print("177:",string({'a':5,'b':3,'c':9}))

#178.Subtract Dictionaries
def subtract(d1,d2):
	new_dic = {}
	for key,value in d1.items():
		if key not in d2:
			new_dic[key] = value
	return new_dic
	
print("178:",subtract({'A':17,'B':31,'C':42,'D':7,'E':46,'F':39},{'D':8,'E':3,'F':2,'g':5}))

#179.Intersection of Two Dictionaries
def intersect(d1,d2):
	new_dic = {}
	for key,value in d1.items():
		if key in d2:
			new_dic[key] = [value,d2[key]]
	return new_dic
	
print("179:",intersect({'A':17,'B':31,'C':42,'D':7,'E':46,'F':39},{'D':8,'E':3,'F':2,'g':5}))

#180.Add Dictionaries
def add(d1,d2):
	new_dic = {}
	for key,value in d1.items():
		if key in d2:
			new_dic[key] = [value,d2[key]]
		else:
			new_dic[key] = value
		
	for key,value in d2.items():
		if key not in new_dic:
			new_dic[key] = value
	return new_dic
	
print("180:",add({'A':17,'B':31,'C':42,'D':7,'E':46,'F':39},{'D':8,'E':3,'F':2,'g':5}))


#181.Login Authentication
def login(u,p):
	d = {'andy':'ilovesusan', 'bob':'ilovemary'}
	if d[u] == p:
		return "ok"
	return 'invalid username or password'
	
print('181',login("andy","ilovesusan"))

#182.Convert Notes to Sound
def convertNotesToSound(s):
	notes = {'a':'la','b':'ti','c':'do','d':'re','e':'mi','f':'fa','g':'sol'}
	new_str = ""
	for c in s:
		new_str+= notes[c]
	return new_str

print("182:",convertNotesToSound("bcbagcgfede"))

#183.SMS
def sms(s):
	pads={'2':'a','22':'b','222':'c','3':'d','33':'e','333':'f','4':'g','44':'h','444':'i',
	      '5':'j','55':'k','555':'l','6':'m','66':'n','666':'o','7':'p','77':'q','777':'r','7777':'s',
		  '8':'t','88':'u','888':'v','9':'w','99':'x','999':'y','9999':'z'}
	l = s.split()
	res = ""
	for item in l:
		if '#' in item:
			temp = item.split("#")
			print(temp)
			index = 0
			length = len(temp) - 1 
			for c in temp:
				res+=pads[c]
				if index < length:
					res+=" "
				index+=1
		else:
			res+=pads[item]
	return res
	
print("183:",sms("444#555 666 888 33#7777 88 7777 44 444"))
	