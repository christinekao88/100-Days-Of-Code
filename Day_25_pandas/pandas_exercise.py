with open ("100 days/Day_25_pandas/weather_data.csv") as data_file:
    data = data_file.readlines()


import csv

with open ("100 days/Day_25_pandas/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    print(data) # 得到一個csv reader object

    temperatures=[]
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    
    print(temperatures)

# 不需要open就可以使用pandas讀取csv
import pandas
data = pandas.read_csv("100 days/Day_25_pandas/weather_data.csv")
print(data)   # dataframe(2-dimensional)

# Get data in columns
print(data['temp']) # Series(1-dimensional)
# pandas已經把columns轉換為屬性
print(data.temp)

# Get data in row - data[要搜尋的欄位==monday](提取data)
print(data[data.day=='Monday']) # 返回monday那一row

# 可以再往下挖掘
monday = data[data.day=='Monday']
monday_temp = int(monday.temp)*9/5+32
print(monday_temp)

# 轉換成dict
data_to_dict = data.to_dict()

# 轉換成list
temp_list = data['temp'].to_list()
print(temp_list) 

# 求平均溫度
average = sum(temp_list)/len(temp_list)
print(average)

print(data['temp'].mean())
print(data['temp'].max())

# 求溫度最高的那一行
print(data[data.temp==data.temp.max()])

# Create a dataframe form scratch
dict = {"student":["Amy","James","Jay"],
"score":[78,98,22]}

student = pandas.DataFrame(dict)
print(student)
student.to_csv("100 days/Day_25_pandas/student.csv")






    
    