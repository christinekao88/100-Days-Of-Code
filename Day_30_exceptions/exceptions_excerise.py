# Read not existing file -> FileNotFoundError ----#
# with open("a_file.txt") as f:
#     f.read()

# Not existing key name ("apple")-> KeyError ---------#
# dic = {"key":"value"}
# value = dic["apple"]

#----- IndexError ---#
# fruit_list = ["apple","orange"]
# fruit = fruit_list[3]

#----- TypeError ---#
# text = 'abc'
# print(text+6)

# Exception Handling - Catching Exception

# sth that might cause an exception
try: 
    file = open("a_file.txt") # open a not existing file
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"]) # not existing key

 # do this if there was an exception
 # 不指定錯誤類型的話表示所有錯誤都會抓
except FileNotFoundError:  
    file = open("a_file.txt", "w")  # create a file
    file.write("Something")

except KeyError as error_message:  # 仍想獲得錯誤訊息
    print(f"The key {error_message} does not exist.")

# do this if there were non exceptions
else: # 如果沒有a_file ，只會執行到exception 
    content = file.read()
    print(content)

# do this no matter what happens
finally: 
    file.close()
    print("File was closed.")
    # create error_message
    # raise TypeError("This is an error that I made up.")


#BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

# 自己抓出不是合理的height
if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)


#----------------------- exercise 1 ---------------------------#
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + " pie")

make_pie(4)
# 試圖獲得index=4 ， 有exception的話print("fruit pie") ，沒有exception的話print(fruit + " pie")

#----------------------- exercise 2 ---------------------------#
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError: 
        # post['Likes']=0
        pass # 沒有exception的才計算，要不就跳過
        
    


print(total_likes)








