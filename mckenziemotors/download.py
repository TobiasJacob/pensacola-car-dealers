import requests

url = lambda i: 'https://www.mckenziemotors.com/VehicleSearchResults?search=preowned&sort=salePrice%7Casc&limit=24&offset=' + str(24 * i)

for i in range(5):
    with open(f'data{i}.html', 'w') as f:
        x = requests.get(url(i))
        f.write(x.text)