import requests
from datetime import datetime

USERNAME = "christine"
TOKEN = "token"
GRAPH_ID ="graph1"

# step 1 : Create your own token and username (post request)
pixela_endpoint = "https://pixe.la/v1/users"

# 自建帳號密碼
user_params = {
    "token":TOKEN,
    "username":USERNAME, 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@christine , it is your profile page!","isSuccess":true}

# step 2 : Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# 請求體並未提供身分認證的key，因此還需要request header-> 會去尋找我們用來註冊的token(也是一種驗證身分的方式)
headers = {
    'X-USER-TOKEN':TOKEN
    }

graph_config = {
    "id":"graph1",  # graph id
    "name":"WorkOUT Graph",    # graph name
    "unit":"minutes",        # 要追蹤的計量單位 ex:km
    "type":"int",           # unit's datatype
    "color":"momiji",
    # "timezone":"Asia/Taipei",
    # "isSecret":True,
    # "publishOptionalData":False
    }

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

# step 3 : Get the graph! https://pixe.la/v1/users/christine/graphs/graph1.html
# step 4 : Post value to the graph

# today=datetime.now()
today=datetime(year=2021,month=6,day=5)
# print(today.strftime("%Y%m%d"))
TIME = today.strftime("%Y%m%d")

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {    
    "date":TIME,
    "quantity":input("How many minutes have you workout today ? "),  # 多少分鐘
    }
response = requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
print(response.text)

# step 5 : Update value to the graph
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TIME}"
pixel_update_config = {
    "quantity":"20",
    }
# response = requests.put(url=pixel_update_endpoint,json=pixel_update_config,headers=headers)
# print(response.text)

# step 6 : Delete a pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TIME}"

# response = requests.delete(url=pixel_delete_endpoint,headers=headers)
# print(response.text)
