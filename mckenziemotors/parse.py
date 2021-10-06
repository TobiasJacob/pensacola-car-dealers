import json
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

cars = []

for i in range(5):
    with open('data' + str(i) + '.html', 'r') as file:
        fileContent = file.read()
        soup = BeautifulSoup(fileContent, 'html.parser')
        hits = soup.find_all(itemtype="http://schema.org/Car")
        for hit in hits:
            make = hit.find('span', class_='make').contents[0].strip()
            milage = hit.find(template="vehicleIdentitySpecs-miles").find(class_="value").contents[0].strip().replace(',', '')
            price = hit.find(class_="primary-price").find(**{'not': "pinBasedDealerPricingFeatureEnabled"}).contents[0].strip()[1:].replace(',', '')
            vin = hit.find(template="vehicleIdentitySpecs-vin").find(class_="value").contents[0].strip()

            cars.append(
                (
                    'Mc Kenzie Motors',
                    make,
                    hit.find('span', class_='model').contents[0].strip(),
                    hit.find('span', class_='year').contents[0].strip(),
                    milage,
                    price,
                    vin
                )
            )
            print(cars[-1])


dataFrame = pd.DataFrame(cars, columns = ['Dealer', 'Manufacturer', 'Model', 'Year', 'Mileage', 'Price', 'VIN'])
dataFrame.to_csv('mckenziemotors.csv')