#Example 1

def greet ():
    print("Hello, Riley!")

def add_numbers():
    num1 = 5
    num2 = 10
    result = num1 + num2
    print("The sum of", num1, "and", num2, "is", result)

greet()
add_numbers()

print("\n")

#Example 2

def greet(name):
    print(f"Hello, {name}!")

greet("Riley")
greet("Alice")
greet("Bob")    


print("\n")

#Example 3

def add_numbers(a,b):
    return a + b

#Call the function with paremeters
result1 = add_numbers(5, 10)
result2 = add_numbers(2.5, 4.5)

print(result1)
print(result2)


print("\n")

#Example 4

count = 0

def increment():
    global count #declare counst as global to modify it inside the function
    count += 1
    print(f"count inside functions: {count}")


increment()
increment()

print(f"count outside function: {count}")


print("\n")

#Example 5

total_sum = 0

def add_to_sum(num):
    global total_sum
    total_sum += num

def display_sum():
    print(f"Total sum: {total_sum}")


add_to_sum(5)
add_to_sum(10)
add_to_sum(20)
display_sum()



print("\n")
#Example 6
def add(a,b):
    return a + b

def multiply(x,y):
    return x * y

def add_and_multiply(a,b, c):
    sum_result = add(a,b)
    product_result = multiply(sum_result, c)
    return product_result

result = add_and_multiply(2, 3, 4)
print(result) #output: 20