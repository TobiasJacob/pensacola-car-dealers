import json
import numpy as np
import pandas as pd


cars = []

for i in range(16):
    file = open('data.json', 'r')
    fileContent = file.read()
    file.close()
    data = json.loads(fileContent)
    hits = data['vehicles']
    for hit in hits:
        cars.append(
            (
                'Hill Kelly Dodge',
                hit['make'],
                hit['model'],
                hit['year'],
                hit['mileage'],
                hit['pricing']['data']['final'],
                hit['vin']
            )
        )


dataFrame = pd.DataFrame(cars, columns = ['Dealer', 'Manufacturer', 'Model', 'Year', 'Mileage', 'Price', 'VIN'])
dataFrame.to_csv('hillkelly.csv')