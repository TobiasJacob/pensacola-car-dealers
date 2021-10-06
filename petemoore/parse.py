import pandas as pd
from bs4 import BeautifulSoup


cars = []
for i in range(5):
    file = open('page' + str(i) + '.html', 'r')
    fileContent = file.read()
    file.close()

    soup = BeautifulSoup(fileContent, 'html.parser')


    results = soup.find_all(itemtype='http://schema.org/Car')
    for car in results:
        make = car.find(class_='make').contents[0].strip()
        label = car.find(class_='model').contents[0].strip()
        year = car.find(class_='year').contents[0].strip()

        milage = car.find(template="vehicleIdentitySpecs-miles").find(class_="value").contents[0].strip().replace(',', '')
        price = car.find(class_="pinBasedPricingDisabled").find(itemprop="price").contents[0].strip()[1:].replace(',', '')
        vin = car.find(template="vehicleIdentitySpecs-vin").find(class_="value").contents[0].strip()
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
