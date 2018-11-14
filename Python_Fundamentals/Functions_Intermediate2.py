# Functions Intermediate 2

# Problem 1

x = [ [5,2,3], [10,8,9] ]

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].

x[1] = [15,8,9]
print(x)

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?

students[0] = {'first_name': 'Michael', 'last_name': 'Bryant'}
print(students)

# For the sports_directory, how would you change 'Messi' to 'Andres'?

sports_directory['soccer'] = ['Andres', 'Ronaldo', 'Rooney']
print(sports_directory)

# For z, how would you change the value 20 to 30?

z = [ {'x': 10, 'y': 30} ]
print(z)

# Problem 2 - Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDict(dict):
    for student in students:
        for key, val in student.items():
            print(key, " - ", val)

iterateDict(students)

# Problem 3 - Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output first names

def iterateDict2(lookup, dict):
    for student in students:
        print(student[lookup])

iterateDict2('first_name', students)

# Problem 4 - Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has.  For example, printDojoInfo(dojo)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printDojoInfo(list):
    for key in dojo:
        print(len(dojo[key]))
        print(key)
        for val in dojo[key]:
            print(val)

printDojoInfo(dojo)
