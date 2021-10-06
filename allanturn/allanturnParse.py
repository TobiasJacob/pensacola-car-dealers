import json
import numpy as np
import pandas as pd


cars = []

for i in range(16):
    file = open('allanturnResp' + str(i) + '.json', 'r')
    fileContent = file.read()
    file.close()
    data = json.loads(fileContent)
    hits = data['results'][0]['hits']
    for hit in hits:
        cars.append(
            (
                'Allan Turner',
                hit['make'],
                hit['model'],
                hit['year'],
                hit['miles'],
                hit['our_price'],
                hit['vin']
            )
        )


dataFrame = pd.DataFrame(cars, columns = ['Dealer', 'Manufacturer', 'Model', 'Year', 'Mileage', 'Price', 'VIN'])
dataFrame.to_csv('allanturnParsed.csv')