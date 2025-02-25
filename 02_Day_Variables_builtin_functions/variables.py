#Day 2: 30 Days of python programming

# Creating Variables in Python: 

first_name = 'Sofia'
last_name = 'Lozano'
full_name = 'Sofia Lozano Samper'
country = 'United States'
city = 'Atlanta'
age = '22'
year = '2025'
is_married = False
is_true = True
is_light_on = True

# Declaring multiple variables in one line: 

first_name, last_name, country, age, is_married = 'Sofia', 'Lozano', 'United States', '22', False 

#Checking variable types: 
print(type(first_name))
print(type(last_name))
print(type(full_name))
frint(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#Using the len() built-in function, find the length of your first name
print(len("Sofia"))

#Compare the length of your first name and your last name
print(len("Sofia", "Lozano"))

#Declare 5 as num_one and 4 as num_two
num_1 = 5
num_2 = 4

#Add num_one and num_two and assign the value to a variable total
total = num_1 + num_2

#Subtract num_two from num_one and assign the value to a variable diff
diff = num_1 - num_2

#Multiply num_two and num_one and assign the value to a variable product
product = num_1 * num_2

#Divide num_one by num_two and assign the value to a variable division
division = num_1 / num_2

#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_1 % num_2

#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_1 ** num_2

#Find floor division of num_one by num_two and assign the value to a variable floor_division (rounds the results down to nearest whole number)
floor_division = num_one // num_two 

#The radius of a circle is 30 meters.

radius = 30

    #Calculate the area of a circle and assign the value to a variable name of area_of_circle

area_of_circle = 3.14 *(radius * radius)

    #Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

circum_of_circle = 2*3.14*radius

    #Take radius as user input and calculate the area.

radius = input('What is the radius?:")
print(area_of_circle)


#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

person_info = {
    'first_name': 'Sofia', 
    'lastname': 'Lozano', 
    'country': 'United States', 
    'city': 'Atlanta'
}


#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
            

# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
