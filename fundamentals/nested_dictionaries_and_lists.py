x = [ [5,2,3], [10,8,9] ]
students = [
    {"first_name":  "Michael", "last_name" : "Jordan"},
    {"first_name" : "John", "last_name" : "Rosales"}
]
sports_directory = {
    "basketball" : ["Kobe", "Jordan", "James", "Curry"],
    "soccer" : ["Messi", "Ronaldo", "Rooney"]
}
z = [ {"x": 10, "y": 20} ]

#Change the value 10 in x to 15. Once you"re done, x should now be [ [5,2,3], [15,8,9] ].
print(x)
x[1][0] = 15
print(x)

#Change the last_name of the first student from "Jordan" to "Bryant"
students[0]["last_name"] = "Bryant"
print(students[0])

#In the sports_directory, change "Messi" to "Andres"
sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"])

#Change the value 20 in z to 30
z[0]["x"] = 30
print(z[0])

# #=========== 2 ===========
students = [
    {"first_name":  "Michael", "last_name" : "Jordan"},
    {"first_name" : "John", "last_name" : "Rosales"},
    {"first_name" : "Mark", "last_name" : "Guillen"},
    {"first_name" : "KB", "last_name" : "Tonel"} ]

def iterateDictionary(some_list):
    for key in some_list:
        print(key)

iterateDictionary(students) 
# should output: (it"s okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#=========== 3 ===========

def iterateDictionary2(key_name, some_list):
#    i=0
    for x in some_list:
        print(x[key_name]) # print([students[i]][key_name]) old - not great, its alot of extras along with the manually counting i variable.
#        i+=1 #don't need i to manually count. x is already doing that in the loop

iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

#=========== 4 ===========

dojo = {
"locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
"instructors": ["Michael", "Amy", "Eduardo", "Josh", "Graham", "Patrick", "Minh", "Devon"]
}
#print(dojo.keys())

def printInfo(some_dict):
    for x in some_dict.keys():
        print(len(some_dict[x]), x)
        for y in range(0,len(some_dict[x])): 
            print(some_dict[x][y])

printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon