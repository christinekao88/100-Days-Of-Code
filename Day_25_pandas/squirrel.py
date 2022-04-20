import pandas

data = pandas.read_csv("100 days/Day_25_pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count= len(data[data['Primary Fur Color']=='Gray'])
red_count= len(data[data['Primary Fur Color']=='Cinnamon'])
black_count= len(data[data['Primary Fur Color']=='Black'])



df = pandas.DataFrame({'Fur color': ['gray', 'Cinnamon','black'],
                   'Count': [gray_count, red_count,black_count]})

df.to_csv("100 days/Day_25_pandas/Squirrel_Fur_color.csv",index=False)