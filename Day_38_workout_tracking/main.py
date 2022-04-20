import os
import requests
from datetime import datetime

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_parameters = {
    "query": exercise_text,
    "gender": "female",
    "weight_kg": 65.5,
    "height_cm": 152.64,
    "age": 35
}

exercise_response = requests.post(exercise_endpoint, json=exercise_parameters, headers=headers)
exercise_result = exercise_response.json()
# print(exercise_result['exercises'])

#---------------------------- Sheety API ------------------------------#
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
user_name = os.getenv("user_name")
user_password = os.getenv("user_password")
token = os.getenv("token")

##  Getting rows

from requests.auth import HTTPBasicAuth
# No Authentication  
sheety_response = requests.get(SHEETY_ENDPOINT)

# Basic Authentication:
sheety_response = requests.get(SHEETY_ENDPOINT,auth=HTTPBasicAuth(user_name, user_password))

# Bearer Authentication:
headers = {"Authorization": token}
sheety_response = requests.get(SHEETY_ENDPOINT,headers=headers)

sheety_result = sheety_response.json()['workouts']
sheety_id = sheety_result[0]['id']
print(sheety_result)


## Add a row

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
for exercise in exercise_result['exercises']:
    # print(f'第一項運動 : {exercise}')
    sheet_inputs = {
        "workout": {
            "date": date,
            'time':time,
            'exercise':exercise["name"].title(),
            'duration':exercise['duration_min'],
            'calories': exercise['nf_calories'],
            # 'id':int(sheety_id)+1
        }
    } 
    sheety_response = requests.post(SHEETY_ENDPOINT,json=sheet_inputs)
    sheety_result = sheety_response.json()
    print(sheety_result)