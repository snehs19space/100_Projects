# 🛠️ Python Exception Handling

This provides a summary of different types of exceptions in Python, examples of how they occur, and how to handle them using various constructs such as `try-except`, `assert`, and manual `raise` statements.


## Common Exception Examples

### 🔸 Division by Zero
```python
print(15 / 0)  # ZeroDivisionError
```

### 🔸 Syntax Error
```python
print(15/0))  # SyntaxError: unmatched ')'
```


## Raising Exceptions

### 🔹 Raise ValueError Based on Condition
```python
name = input("Enter your Name: ")
age = input("Enter your Age:")
print("Your name is:", name)
if age < 18:
     raise ValueError("Error: You need to be over 18.")
else:
     print("Your age is:", age)
```

### 🔹 Raise General Exception
```python
num = input("Enter a Number: ")
if num < 5:
     raise Exception("Error: Value needs to be greater than 5.")
else:
     print("Your number is:", num)
```


## AssertionError

### 🔹 Assert Condition
```python
x = 1
y = 0
assert y != 0, "Invalid Operation"
print(x / y)
```

### 🔹 Using assert in a Function
```python
def print_age(age):
     assert age > 0, "The value of age has to be greater than Zero."
     print("Your age is:", age)
print_age(8)
```

## Try-Except Blocks

### 🔹 Basic try-except
```python
try:
     num1 = 4
     num2 = 0
     print(num1 / num2)
     print("End of try block.")
except ZeroDivisionError as e:
     print(e)
```

### 🔹 try-except-else
```python
try:
     num1 = 4
     num2 = 8
     result = num1 / num2
     print("End of try block.")
except TypeError as e:
     print(e)
else:
     print("No exception raised.")
```

### 🔹 try-except-finally
```python
try:
    file = open("example.txt")
except FileNotFoundError as e:
    print(e)
finally:
    file.close()
```

> ⚠️ Note: In the final example, if the file does not exist, calling `file.close()` in the `finally` block without confirming that the file was successfully opened will raise another exception.

## 


## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/snehs19space/100_Projects/blob/main/LICENSE) file for details.
