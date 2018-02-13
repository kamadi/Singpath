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
