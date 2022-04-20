# 此時*args = (3,5,6,7,4,32,3,4)
def add(*args):
    sum = 0
    for n in args:
        sum+=n
    return sum

print(add(3,5,6,7,4,32,3,4))

# n為normal position argument
def calculate(n,**kwargs):
    print(kwargs)  # 此時**kwargs = {'add': 3, 'multiply': 5} -> dictionary
    print(kwargs["add"])  # 3
    for key ,value in kwargs.items():
        print(key)
        print(value)
    
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)
    
# 此時n=2，其餘為dictionary
calculate(2,add=3,multiply=5)

class Car:
    # **kwargs代表所有可選參數
    def __init__(self,**kwargs):
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]

        # 利用get function依樣只需要傳入key可以得到value, 好處是如果key不存在kwargs dict()的話，他只會返回none，不會給我們一個錯誤
        self.type = kwargs.get("type")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan",model='GT-R')
print(my_car.make)

my_car = Car(make="Nissan")




