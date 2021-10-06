import requests

url = lambda i: 'https://www.petemoorechevrolet.com/VehicleSearchResults?search=preowned&sort=salePrice%7Casc&limit=100&offset=' + str(i * 100)

for i in range(0, 5):
    x = requests.get(url(i))
    file = open('page' + str(i) + '.html', 'w')
    file.write(x.text)
    file.close()
