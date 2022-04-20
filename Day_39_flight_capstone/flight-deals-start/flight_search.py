import requests
from flight_data import FlightData
from pprint import pprint

TEQUILA_ENDPOINT="https://tequila-api.kiwi.com"
TEQUILA_API_KEY="TEQUILA_API_KEY"


class FlightSearch:

    def __init__(self):
        self.code_codes=[]

    def get_destination_data(self, city_name):

        print("get destination codes triggered")
    
        headers = {
            "apikey": TEQUILA_API_KEY
            }
        
        for city in city_name:
            query = {
                "term": city, 
                "location_types": "city"
                }
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/locations/query", 
                headers=headers, 
                params=query
                )

            results = response.json()["locations"]
            # print(results)
            
            code = results[0]["code"]

            self.code_code.append(code)
            return self.code_codes

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        print(f"Check flights triggered for {destination_city_code}")

        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "TWD"
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )
        
        try:
            data = response.json()["data"][0]
            print(f"{destination_city_code} {data['price']}")

        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            # return None

            ########################################################################
            # There are a lot of popular destinations that our customers will want to go to that don't have direct flights. e.g. Bali
            # If a flight is not found, check to see if there are flights with 1 stop
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]
            pprint(data)
            #  the "route" key value pair you get back from the API now contains a list with 4 items. 
            # [origin -> stop_over, stop_over -> destination, destination -> stop_over, stop_over -> origin].
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
            
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            # print(f"{flight_data.destination_city}: £{flight_data.price}")
            print(f"{flight_data.destination_city}: NT {flight_data.price}")

            return flight_data
