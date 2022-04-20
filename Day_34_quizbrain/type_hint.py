# 可以先申明變數的data type以防止出錯
age : int
age = 12
age ="wer"

# datatype in function
# 指定參數datatype，可預先避免錯誤，也可以指定輸出的datatype -> # 預期返回bool
def police_check(age:int) -> bool: 
    if age>19:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(2):
    print("You may pass")
else:
    print("Pay a fine")

# TypeError
if police_check("20"):
    print("You may pass")
else:
    print("Pay a fine")