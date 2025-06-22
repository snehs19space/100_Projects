# Division by Zero Error
# print(15/0)

# Syntax Error
# print(15/0))

# Raising an Exception
'''
name = input("Enter your Name: ")
age = input("Enter your Age:")
print("Your name is:",name)
if age < 18:
    raise ValueError("Error: You need to be over 18.")
else:
    print("Your age is:",age)
'''

'''
num = input("Enter a Number: ")
if num < 5:
    raise Exception("Error: Value need to be greater than 5.")
else:
    print("Your number is:",num)
'''

# AssertionError Exception
'''
x = 1
y = 0
assert y != 0, "Invalid Operation"
print(x/y)
'''

'''
def print_age(age):
    assert age > 0, "The value of age has to be greater than Zero."
    print("Your age is:",age)

print_age(8)
'''

# try - except
'''
try:
    num1 = 4
    num2 = 0
    print("End of try block.")
except ZeroDivisionError as e:
    print(t)
'''

# try - except - else
'''
try:
    num1 = 4
    num2 = 8
    result = num1/num2
    print("End of try block.")
except TypeError as e:
    print(e)
else:
    print("No exception raised.")
'''

# try - except - finally
try:
    file = open("example.txt")
except FileNotFoundError as e:
    print(e)
finally:
    file.close()