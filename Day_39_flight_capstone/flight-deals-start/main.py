# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

ORIGIN_CITY_IATA = "TPE"

#----------- 1. get goole sheet's data (sheety API) ------------#
data_manager = DataManager()
# sheet_data1 = data_manger.destination_data
sheet_data = data_manager.get_destination_data()
# sheet_data3 = data_manager.destination_data
# print(type(sheet_data))

flight_search=FlightSearch()

notification_manager = NotificationManager()

#-----------  2. turn city name to iatacode (TEQUILA API) ------------#
for row in sheet_data:
    # 將row['iataCode']的值用return的iata_code 取代
    # row['iataCode'] = flight_search.get_destination_data(row['city']) 

    # 更新data_manager.destination_data 為sheet_data
    data_manager.destination_data = sheet_data

#-----------  3. update data 成新的iataCode (sheety API) ------------#
# update_sheet = data_manager.update_destination_data()
# print(update_sheet)

#-----------  4. 取得航班資訊(TEQUILA API) ------------#
today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)

for row in sheet_data:
    # print(row['iataCode'])
    flight_data = flight_search.check_flights(
        ORIGIN_CITY_IATA, 
        row['iataCode'] , 
        today,
        six_month_from_today
        )
    
    #-----------  5. 通知(TWILIO API) ------------#
    if flight_data.price < row["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}."
        )