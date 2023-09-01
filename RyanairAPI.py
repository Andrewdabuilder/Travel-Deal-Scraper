from datetime import datetime, timedelta
from ryanair import Ryanair

api = Ryanair(currency="EUR")  # Euro currency, so could also be GBP etc. also
tomorrow = datetime.today().date() + timedelta(days=1)
tomorrow_1 = tomorrow + timedelta(days=1)
next_week = tomorrow + timedelta(days=7)
List_of_countries = ["IE","GB"]


# The below calls the API
trips = api.get_cheapest_return_flights("DUB", tomorrow, tomorrow, tomorrow_1, next_week, any(List_of_countries))
print(trips[0])
print(len(trips))