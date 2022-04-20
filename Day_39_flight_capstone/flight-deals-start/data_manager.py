import requests
from requests.auth import HTTPBasicAuth

SHEETY_ENDPOINT = "endpoint"

class DataManager:
    def __init__(self):
        self.destination_data={}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_ENDPOINT)
        self.destination_data= response.json()['prices']
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            # print(city)
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
    
    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data