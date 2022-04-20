################### Squaring Numbers ###########################

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:
squared_numbers = [num**2 for num in numbers]

#Write your code 👆 above:

# print(squared_numbers)

################### Even Numbers ######################################
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:
result = [num for num in numbers if num%2==0] 

#Write your code 👆 above:

# print(result)


#################### equal number #######################################

with open (r"100 days\Day_26\file1.txt") as f:
    file_1 = f.readlines()
    
with open (r"100 days\Day_26\file2.txt") as f:
    file_2 = f.readlines()
    
result = [int(num) for num in file_1 if num in file_2]
# Write your code above 👆

# print(result)

######################## excerise ###################################

#For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#List Comprehension
new_list = [n + 1 for n in numbers]

#String as List
name = "Angela"
letters_list = [letter for letter in name]

#Range as List
range_list = [n * 2 for n in range(1, 5)]

#Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {key:value for (key,value) in student_grades.items() if student_grades[key]>60}
# print(passed_students)

################ Dictionary Comprehension 1 ######################
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
result = {word:len(word) for word in sentence.split()}
print(result)

################ Dictionary Comprehension 2 ######################
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:
weather_f ={key:(value * 9/5) + 32 for (key,value) in weather_c.items()}
print(weather_f)

######################## pandas ###########################
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}


# looping through dictionaries 
for (key,value) in student_dict.items():
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# loop through a dataframe 
for (key,value) in student_data_frame.items():
    #Access key and value
    print(value)

# pandas 有自己的in-built loop
for (index ,row) in student_data_frame.iterrows():
    # Access index and row : 得到的每一row都是一個pandas series object
    print(row)
    # Access row.student or row.score ->可以獲取每列下的值
    print(row.Student)
    print(row.score)

    # 取得Alex的分數
    if row.Student == "Alex":
        print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}