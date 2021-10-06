import pandas as pd
from bs4 import BeautifulSoup
import json

cars = []
for i in range(5):
    with open('petemoorechevy_production_inventory.json', 'r') as file:
        data = json.load(file)

    for car in data["hits"]:
        make = car["make"]
        label = car["model"]
        year = car["year"]

        milage = car["miles"]
        price = car["our_price"]
        vin = car["vin"]
        cars.append(
            (
                'Pete Moore',
                make,
                label,
                year,
                milage,
                price,
                vin
            )
        )
        print(cars[-1])


dataFrame = pd.DataFrame(cars, columns = ['Dealer', 'Manufacturer', 'Model', 'Year', 'Mileage', 'Price', 'VIN'])
dataFrame.to_csv('petemoore.csv')
