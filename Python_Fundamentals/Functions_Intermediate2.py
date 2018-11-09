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

# For z, how would you change the value 20 to 30?

# Problem 2
