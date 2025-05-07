#String - variable words
first_name = "chefe"
food = "chocolate"
email = "chefe123@fake.com"

print(f"hello {first_name}")
print(f"You like {food}?")
print (f"your email is: {email}?")

#Integers - numbers, value
age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f'You are buying {quantity} pizzas.')
print(f'There are {num_of_students} in this college.')

#Float - have decimal
price = 10.99
gpa = 3.2
distance = 234.67

print(f'The price is ${price}.')
print(f'Your gpa is {gpa}.')
print(f'The distance between Rio Claro and São Paulo is {distance}km.')

#Boolean - have only two variables

is_student = True
for_sale = False
is_online = True

if is_student:
    print('You are a student.')
else:
    print('You are NOT a student.')

print(f'Are you a student?: {is_student}.')

if for_sale:
    print('That item is for sale.')
else:
    print(f'That item is NOT for sale.')

if is_online:
    print('He is online.')
else:
    print('He is NOT onlien.')
