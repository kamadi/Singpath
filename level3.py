# 26
def square(param):
    return param * param


print "26:", square(4)


# 27
def increment(param):
    return param + 1


print "27:", increment(5)


# 28
def product(a, b):
    return a * b


print "28:", product(2, 6)


# 29
def sum(a, b):
    return a + b


print "29:", sum(5.6, 7)


# 30
def double_word(s):
    return str(s) + str(s)


print "30", double_word("test")


# 31
def double_word(s, n):
    return s * n


print "31:", double_word("test", 7)

# 33

import math


def area_of_circle(radius):
    return math.pi * math.pow(radius, 2)


print "33:", area_of_circle(5)


# 34
def radian(angle):
    return (angle * math.pi) / 180


print "34:", radian(180)


# 35
def cosine(angle):
    return math.cos(radian(angle))


print "35:", cosine(45)


# 36
def sandwich(bread, meat="turkey", cheese=None):
    res = bread + " bread sandwith with " + meat
    if cheese != None:
        res += " and " + cheese + " cheese"
    return res


print "36:", sandwich("wheat", cheese="American")


# 37
def CurryPuff(money, type="Chicken"):
    if type == "Fish":
        return money * 1.4
    return money * 1.2


print "37:", CurryPuff(3, "Fish")


