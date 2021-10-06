import pandas as pd
from bs4 import BeautifulSoup

cars = []
file = open('website.html', 'r')
fileContent = file.read()
file.close()

soup = BeautifulSoup(fileContent, 'html.parser')
results = soup.find(class_='inv-repeater update-vehicles')


results = results.find_all(class_='row no-gutters invMainCell')
for car in results:
    label = car.find(class_='d-md-none titleWrapPhoneView').find('a').contents[0].strip()
    year = label.split(" ")[0]
    make = label.split(" ")[1]

    milage = car.find(class_="optMileage").contents[2].strip().replace(',', '')
    VIN = car.find(class_="optVin").contents[2].strip().replace(',', '')
    price = car.find(class_="price-1").contents[0].strip()[1:].replace(',', '')
    cars.append(
        (
            'Car Deals',
            make,
            label.split(" ")[2],
            year,
            milage,
            price,
            VIN
        )
    )
    print(cars[-1])


dataFrame = pd.DataFrame(cars, columns = ['Dealer', 'Manufacturer', 'Model', 'Year', 'Mileage', 'Price', 'VIN'])
dataFrame.to_csv('cardeals.csv')
