# open (in-built method)
file = open("100 days\Day_24_snake_game_modify\my_file.txt")
# read file -> 文件內容以字串形式返回
contents = file.read()
print(contents)
# open 會占用電腦資源
file.close()

# 用with可以直接管理文件，完成後即會關閉文件 # 預設為read only 
with open("100 days\Day_24_snake_game_modify\my_file.txt") as f :
    # read
    contents = f.read()
    print(contents)

with open("100 days\Day_24_snake_game_modify\my_file.txt", mode="a") as f :
    # write -> mode='w' 會覆蓋所有文字
    # write -> mode='a' append原有文字
    f.write("\nNew Text.")

# create 不存在的file 
with open("100 days\Day_24_snake_game_modify\/new_file.txt", mode="w") as f :
    # write -> mode='w' 會覆蓋所有文字
    # write -> mode='a' append原有文字
    f.write("\nNew Text.")

# 如果檔案放桌面
with open("../../../../\/new_file2.txt", mode="w") as f :
    # write -> mode='w' 會覆蓋所有文字
    # write -> mode='a' append原有文字
    f.write("\nssssss Text.")