import json
import numpy as np
import pandas as pd


cars = []

file = open('data.json', 'r')
fileContent = file.read()
file.close()
data = json.loads(fileContent)
hits = data
for hit in data:
    cars.append(
        (
            'Downtown Motors',
            hit['make'],
            hit['model'],
            hit['year'],
            hit['mileage'],
            hit['price'],
            hit['vin']
        )
    )


dataFrame = pd.DataFrame(cars, columns = ['Dealer', 'Manufacturer', 'Model', 'Year', 'Mileage', 'Price', 'VIN'])
dataFrame.to_csv('downtownMotors.csv')