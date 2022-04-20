"""
Day 9 - Beginner - Dictionaries, Nesting and the Secret Auction
"""

#------------------------ Dictionaries ------------------------#

# 最後放逗號可以隨時新增
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
     "Function": "A piece of code that you can easily call over and over again.",
     123:456,
}

# Retrieving from dictionary
print(programming_dictionary["Bug"])
print(programming_dictionary[123])

# Adding new item to dictionary
programming_dictionary["Loop"]="The action of sth over and over again"

# Create empty dictionary
empty_dictionary={}

# wipe an existing dictionary
programming_dictionary={}
print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary[123]=789
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    # get key
    print(key)
    # get value
    print(programming_dictionary[key])

#------------------------ Grading Program ------------------------#
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores :
    score = student_scores[key]
    if score <= 100 and score>90:
        student_grades[key]= "Outstanding"
    elif score>80:
        student_grades[key]="Exceeds Expectations"
    elif score>70:
        student_grades[key]="Acceptable"
    elif score <= 70:
        student_grades[key]="Fail"
# 🚨 Don't change the code below 👇
print(student_grades)

#------------------------ Nesting ------------------------#
# Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

# to be added to the travel_log. 👇

def add_new_country(country,visits,cities):
    add_dic={
        "country": country,
        "visits": visits,
        "cities": cities}

    travel_log.append(add_dic)
    
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
i=len(travel_log)-1
a=travel_log[i]["country"]
b=travel_log[i]["visits"]
print(f'You\'ve visited {a} {b} times.')


#------------------------ Secret Auction ------------------------#
from replit import clear
#HINT: You can call clear() to clear the output in the console.
from replit import clear
from Day_9_art import logo
print(logo)
print("Welcome to the secret auction program")

def find_highest(bidding_dic):
    highest=0
    winner=''
    for key in dic:
        price=int(dic[key])
        if price > highest:
            highest = price
            winner=key
    print(f"{winner} is the winner with ${highest}")

dic={}
keep=True
while keep:
    name=input("What's your name ? ")
    bid=input("What's your bid ? $ ")
    dic[name]=bid
    other=input('Are there any other bidders ? Type "yes" or "no"\n').lower()
    if other == "yes":
        clear()
    else:
        keep=False
        find_highest(dic)


