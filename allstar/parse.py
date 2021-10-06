import json
import numpy as np
import pandas as pd


cars = []

for i in range(2):
    file = open('allstar' + str(i) + '.json', 'r')
    fileContent = file.read()
    file.close()
    data = json.loads(fileContent)
    hits = data['Vehicles']
    for hit in hits:
        cars.append(
            (
                'All star',
                hit['Make'],
                hit['Model'],
                hit['Year'],
                hit['Odometer'],
                hit['VehiclePrice'],
                hit['Vin']
            )
        )


dataFrame = pd.DataFrame(cars, columns = ['Dealer', 'Manufacturer', 'Model', 'Year', 'Mileage', 'Price', 'VIN'])
dataFrame.to_csv('allstar.csv')