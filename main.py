from functions import parse 
import random
 
# Ask the user to enter a lower and an upper bound divided by a comma
user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10)")
 
# Parse the user string by calling the parse function
parsed = parse(user_input)
# print(parsed['upper_bound'])
# Pick a random int between the two numbers
rand = random.uniform(parsed['lower_bound'], parsed['upper_bound'])
 
print(rand)













# import random
# lower = int(input("Enter the lower bound: "))
# higher = int(input("Enter the higher bound: "))

# num = random.randint(lower, higher)
# print(num)

# import json
# with open('questions.json', 'r') as file:
#     content = file.read()

# data = json.loads(content)

# score = 0
# for question in data:
#     print(question["question"])
#     for index, choice in enumerate(question["choices"]):
#         print(f"{index + 1}. {choice}")
#     user_choice = int(input("Enter your answer: "))
#     compare_user_choice = user_choice - 1
#     user_answer = question["choices"][compare_user_choice]
#     if user_answer == question["answer"]:
#         score = score + 1
#         print("Correct answer is: " + question["answer"])
#     else:
#         print("Correct answer is: " + question["answer"])

# print(f"score = {score}")






















# import functions
# while True:
#     user_action = input("What do you want to do? (add/show/remove/update/count): ")
#     if user_action == 'add':
#         todo = input("Add a todo ...")
#         functions.add_todo(todo)
#     elif user_action == 'show':
#         todos = functions.get_todos()
#         for index, todo in enumerate(todos):
#             index = index + 1
#             print(f"{index}. {todo}")
#     elif user_action == 'remove':
#         todo = input("A number of todo to remove ...")
#         functions.remove_todo(todo)
#     elif user_action == 'update':
#         todo = input("A number of todo to update ...")
#         new_todo = input("Enter the new todo text ...")
#         functions.update_todo(todo, new_todo)
#     elif user_action == 'count':
#         print(functions.count_todo())


# def strength(password):
#     upper = digit = passlength = False
#     if any(char.isupper() for char in password):
#         upper = True
#     if any(char.isdigit() for char in password):
#         digit = True
#     if len(password) > 8:
#         passlength = True
    
#     validation = upper + digit + passlength
#     if validation == 3:
#         return("Strong password")
#     else:
#         return("Weak password")
    
# print(strength("232fsfdsEff"))



# def list_of_arg(list):
#     length = len(list)
#     total = sum(float(i) for i in list)
#     result = total / length
#     return result
    
# mylist = [10, 20, 30, 40]
# print(list_of_arg(mylist))


# def speed(distance, time):
#     return distance / time
    
# print(speed(300, 5))

# def prepare(text):
#     """ This function takes a string and returns a cleaned up version of it. """
#     text = text.title()
#     text = text.strip()
#     return text
    
# print(prepare("test"))
# print(help(prepare))


# def get_age(year_of_birth, current_year = 2025):
#     age = current_year - int(year_of_birth)
#     return age

# year_of_birth = input("Please enter your year of birth   ")
# your_age = get_age(year_of_birth)
# print(your_age)


# def get_nr_items(user_input):
#     words = user_input.split(",")
#     count = len(words)
#     return count

# print(get_nr_items("john,lisa, teresa"))


# def squareinfo(sl):
#     sqaure = int(sl) * int(sl)
#     return sqaure

# print(squareinfo(7))

# def foo(temperature):
#     if int(temperature) > 7:
#         return "Warm"
#     else:
#         return "Cold"

# print(foo(7))


# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
    
  
# time = calculate_time(100)
# print(time)