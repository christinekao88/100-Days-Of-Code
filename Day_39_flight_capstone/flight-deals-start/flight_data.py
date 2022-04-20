class FlightData:
    
    def __init__(self, price, origin_city,
                 origin_airport, destination_city, 
                 destination_airport, out_date, return_date,
                 stop_overs,via_city):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

        # stop_overs set to 1 
        # via_city as the name of stopover city
        self.stop_overs = stop_overs
        self.via_city = via_city