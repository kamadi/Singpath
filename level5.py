# 79.While Loop
def sum(max):
    i = 1
    sum = 0
    while i <= max:
        sum += i
        i += 1
    return sum


print "79:", sum(3)


# 80.Sum range
def sum_of_range(start, end):
    sum = 0
    while start <= end:
        sum += start
        start += 1
    return sum


print "80:", sum_of_range(-23, -4)


# 81.Sum range by Step
def sum_of_range(start, end, step):
    sum = 0
    while start <= end:
        sum += start
        start += step
    return sum


print "81:", sum_of_range(-2, 100, 5)
