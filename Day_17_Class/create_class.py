# Create Class
class User:
    # initialise attributes (設定attributes初始值)
    # 每一次create object時，都會呼叫一次這個function
    # self 為正在創建或初始化的object
    def __init__(self):
        print("yooooooo")


# Create object from class
user_1 = User()

# Create attributes
user_1.id = '001'
user_1.name = 'angela'

print(user_1.name)

user_2 = User()
user_1.id = '002'
user_1.name = 'jack'

# add attributes
class User2:
    def __init__(self,user_id,username):

        self.id = user_id
        self.username = username
        
        # default attributes value
        self.followers = 0
        self.following = 0

    # 不同於function，method第一個參數都是"self"，當method被調用時，他會知道調用他的對象
    def follow(self,user):
        # 我們關注的user的followers會增加1
        user.followers += 1
        # 自己的following會增加1
        self.following += 1

# Create object from class
user_1 = User2('001','angela')
# print(user_1.id)
# print(user_1.username)
# print(user_1.followers)
user_2 = User2('002','jack')

# user_1(object).follow(method from user_1 object)
# user_1 follow user_2
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


class Car:
    # additional parameters seats
    def __init__(self,seats):
        # self.attributes = parameters (seat)
        self.seats =seats

# 此時my_car.seats = 5
my_car = Car(5)

# 等同於
my_car.seats = 5


class Car2:
    # function attaching to a object called "method"
    def enter_race_mode():
        self.seats =2

# my_car.enter_race_mode()