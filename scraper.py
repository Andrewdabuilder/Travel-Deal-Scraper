import requests
from bs4 import BeautifulSoup


def scrape_flights():
    url = "https://www.exampleairlines.com/flights"  # Replace this with the actual URL

    # Send an HTTP GET request to the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the elements containing flight information
    flights = soup.find_all("div", class_="flight-item")

    flight_results = []
    for flight in flights:
        # Extract flight details
        airline = flight.find("span", class_="airline").text.strip()
        flight_number = flight.find("span", class_="flight-number").text.strip()
        departure_time = flight.find("span", class_="departure-time").text.strip()
        arrival_time = flight.find("span", class_="arrival-time").text.strip()
        price = flight.find("span", class_="price").text.strip()

        # Create a dictionary with the flight details
        flight_info = {
            "Airline": airline,
            "Flight Number": flight_number,
            "Departure Time": departure_time,
            "Arrival Time": arrival_time,
            "Price": price,
        }
        flight_results.append(flight_info)

    return flight_results

if __name__ == "__main__":
    flights = scrape_flights()
    if flights:
        for idx, flight in enumerate(flights, start=1):
            print(f"Flight {idx}:")
            for key, value in flight.items():
                print(f"{key}: {value}")
            print("-" * 30)
    else:
        print("No flights found.")
