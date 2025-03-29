# 1
# Write a function sum_numbers that accepts an arbitrary number of positional arguments and returns their sum.
# Call the function with three numbers.
# Call the function with no arguments and ensure it handles this case gracefully.


# def sum_numbers(*args):
    
#     if len(args) == 0:
#         return 0
#     return sum(args)

# print(sum_numbers(1, 2, 3))  


# print(sum_numbers()) 





# 2
# Write a function display_student_info that accepts any number of keyword arguments and prints them in the format: key: value.
# Call the function with keyword arguments such as name="Alice", age=20, and major="CS".
# Experiment with passing different sets of keyword arguments.


# def display_student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# display_student_info(name="Alice", age=20, major="CS")

# display_student_info(name="Bob", age=22, major="Math", university="XYZ University")
# display_student_info(first_name="Eve", last_name="Smith", year=2025)



# 3
# Write a function order_item that accepts:
# A required item argument.
# A quantity argument with a default value of 1.
# Arbitrary positional arguments (*args) to specify additional options.
# Arbitrary keyword arguments (**kwargs) for customization details



# def order_item(item, quantity=1, *args, **kwargs):
#     print(f"Item: {item}")
#     print(f"Quantity: {quantity}")
    
#     if args:
#         print("Additional options:", args)
    
#     if kwargs:
#         print("Customization details:")
#         for key, value in kwargs.items():
#             print(f"{key}: {value}")


# order_item("Laptop", 2)

# order_item("Phone", 1, "Color: Black", "Screen Size: 6.5 inches", brand="Apple", warranty="1 year")

# order_item("Headphones")




# 4
# Write a function register_user that accepts:
# A required positional argument: username.
# A required keyword-only argument: email.
# Hint: Use * to enforce keyword-only arguments.

# def register_user(username, *, email):
#     print(f"Username: {username}")
#     print(f"Email: {email}")

# register_user("Alice", email="alice@example.com")
# register_user("Bob", email="bob@example.com")





# 5
# Analyze the following code, explain why it raises an error, and fix the function call: 
# def book_ticket(destination, price, discount=0, *extras, **details):
#     print(f"Booking to {destination} for ${price - discount}")
#     if extras:
#         print(f"Extras: {', '.join(extras)}")
#     if details:
#         print(f"Details: {details}")

# book_ticket("Paris", extras=["window seat", "meal"], discount=10, price=100)  # output   # Booking to Paris for $90       # Details: {'extras': ['window seat', 'meal']}     




#  6
# Implement a function process_data that accepts a mix of positional arguments, default arguments, arbitrary positional arguments (*args), and arbitrary keyword arguments (**kwargs).
# Require the first two arguments to be data (a list) and operation (a string that specifies the operation to perform: 'sum', 'multiply', 'filter').
# Optionally accept a threshold parameter with a default value of None. This will only be used for the 'filter' operation.
# Accept additional numbers via *args to be appended to the data list before processing.
# Accept additional processing options through **kwargs, such as:
# reverse (boolean): Whether to reverse the result.
# unique (boolean): Whether to ensure the data list contains unique values before processing.
# Function Behavior:
# If the operation is 'sum', return the sum of the elements in the data list.
# If the operation is 'multiply', return the product of the elements in the data list.
# If the operation is 'filter', return a list of numbers greater than threshold.
# Apply reverse and unique options based on the kwargs values.




# def process_data(data, operation, threshold=None, *args, **kwargs):
    
#     data.extend(args)

    
#     if kwargs.get('unique', False):
#         data = list(set(data))

#     if operation == 'sum':
#         result = sum(data)
#     elif operation == 'multiply':
#         result = 1
#         for num in data:
#             result *= num
#     elif operation == 'filter':
#         if threshold is None:
#             raise ValueError("Threshold must be provided for the 'filter' operation")
#         result = [num for num in data if num > threshold]
#     else:
#         raise ValueError("Invalid operation. Supported operations are 'sum', 'multiply', and 'filter'.")

    
#     if kwargs.get('reverse', False):
#         if isinstance(result, list):  
#             result = result[::-1]

#     return result



# result1 = process_data([1, 2, 3], 'sum', 0, 4, 5, reverse=False, unique=False)
# print(result1)  # Output: 15 (1 + 2 + 3 + 4 + 5)


# result2 = process_data([2, 3, 4], 'multiply', reverse=False, unique=False)
# print(result2)  # Output: 24 (2 * 3 * 4)


# result3 = process_data([1, 2, 3, 5, 6, 6], 'filter', threshold=5, reverse=False, unique=True)
# print(result3)  # Output: [6]

# result4 = process_data([1, 2, 3, 4, 6, 6], 'filter', threshold=3, reverse=True, unique=True)
# print(result4)  # Output: [6, 4, 6]






# 7
# Write a closure that creates a counter. Each call to the inner function should increment the counter by 1 and return the current count.

# def create_counter():
#     count = 0  
    
    
#     def counter():
#         nonlocal count  
#         count += 1
#         return count
    
#     return counter 


# counter_function = create_counter()

# print(counter_function())  # Output: 1
# print(counter_function())  # Output: 2
# print(counter_function())  # Output: 3





# 8
# Create a closure that takes a multiplier as an argument and returns a function that multiplies any given number by that multiplier.

# def create_multiplier(multiplier):
   
#     def multiplier_function(number):
       
#         return number * multiplier
    
#     return multiplier_function  

# multiply_by_5 = create_multiplier(5)

# print(multiply_by_5(10))  # Output: 50
# print(multiply_by_5(3))   # Output: 15

# multiply_by_2 = create_multiplier(2)

# print(multiply_by_2(10))  # Output: 20
# print(multiply_by_2(3))   # Output: 6





# 9
# Write a closure that tracks the number of times a specific function is called.
# def track_calls(func):
#     count = 0  
    
#     def wrapper(*args, **kwargs):
#         nonlocal count  
#         count += 1  
#         print(f"Function has been called {count} times.")
#         return func(*args, **kwargs)  
#     return wrapper  

# @track_calls
# def example_function():
#     print("Function executed.")


# example_function()  # Output: Function has been called 1 times.
#                     #         Function executed.
# example_function()  # Output: Function has been called 2 times.
#                     #         Function executed.
# example_function()  # Output: Function has been called 3 times.
#                     #         Function executed.




# 10
# Create a closure to calculate running totals. Each call to the inner function should add a number to the total and return the updated total.

# def running_total():
#     total = 0  
    
    
#     def add_to_total(number):
#         nonlocal total  
#         total += number  
#         return total 
    
#     return add_to_total  

# total_function = running_total()


# print(total_function(10))  # Output: 10 (Running total: 10)
# print(total_function(5))   # Output: 15 (Running total: 15)
# print(total_function(3))   # Output: 18 (Running total: 18)
# print(total_function(7))   # Output: 25 (Running total: 25)




# 11
# Implement a closure that takes a string as input and allows appending to or resetting the string when the inner function is called.

# def string_manager(initial_string=""):
#     current_string = initial_string  
    
#     def manage_string(action, new_string=""):
#         nonlocal current_string  
        
#         if action == "append":
#             current_string += new_string  
#         elif action == "reset":
#             current_string = new_string  
#         return current_string 
    
#     return manage_string  

# string_function = string_manager()


# print(string_function("append", "Hello, "))  # Output: "Hello, "
# print(string_function("append", "World!"))   # Output: "Hello, World!"


# print(string_function("reset", "New String"))  # Output: "New String"

# print(string_function("append", "Again!"))  # Output: "New StringAgain!"