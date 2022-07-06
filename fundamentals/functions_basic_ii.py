#Countdown
def countdown(num):
    newval = []
    for x in range(num,0,-1):
        newval.append(x)
    return newval
print(countdown(5))

#Print and Return
def print_and_return(list):
    print(list[0])
    return(list[1])
testlist = [1,2]
print(print_and_return(testlist))

#First Plus Length
def first_plus_length(list):
    sum = list[0] + len(list)
    return sum
testlist2 = [1,2,3,4,5]
print(first_plus_length(testlist2))

#Values Greater than Second
def values_greater_than_second(list):
    if len(list) < 2:
        return "False"
    count = 0
    newlist = []
    for x in range(0,len(list)):
        if list[x] > list[1]:
            count = count + 1
            newlist.append(list[x])
    print(count)
    return newlist
testlist3 = [5,2,3,2,1,4]
testlist4 = [3]
print(values_greater_than_second(testlist3))
print(values_greater_than_second(testlist4))

#This Length, That Value
def length_and_value(size,value):
    newlist = []
    for x in range(size):
        newlist.append(value)
    return newlist
print(length_and_value(4,7))
print(length_and_value(6,2))