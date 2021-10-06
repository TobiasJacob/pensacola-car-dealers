import requests


url = 'https://sewjn80htn-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.1.0)%3B%20Browser%20(lite)%3B%20JS%20Helper%20(3.1.1)&x-algolia-api-key=179608f32563367799314290254e3e44&x-algolia-application-id=SEWJN80HTN'
data = lambda i: '{"requests":[{"indexName":"allenturnerhyundai_production_inventory_low_to_high","params":"maxValuesPerFacet=250&hitsPerPage=20&page=' + str(i) + '&facets=%5B%22features%22%2C%22our_price%22%2C%22lightning.lease_monthly_payment%22%2C%22lightning.finance_monthly_payment%22%2C%22type%22%2C%22api_id%22%2C%22year%22%2C%22make%22%2C%22model%22%2C%22model_number%22%2C%22trim%22%2C%22body%22%2C%22doors%22%2C%22miles%22%2C%22ext_color_generic%22%2C%22features%22%2C%22lightning.isSpecial%22%2C%22lightning.locations%22%2C%22fueltype%22%2C%22engine_description%22%2C%22transmission_description%22%2C%22metal_flags%22%2C%22city_mpg%22%2C%22hw_mpg%22%2C%22days_in_stock%22%2C%22lightning.locations.meta_location%22%2C%22lightning.locations.Location%22%5D&tagFilters=&facetFilters=%5B%5B%22type%3AUsed%22%5D%5D"},{"indexName":"allenturnerhyundai_production_inventory_low_to_high","params":"maxValuesPerFacet=250&hitsPerPage=1&page=0&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=type"}]}'

for i in range(16):
    print(i)
    x = requests.post(url, data = data(i))
    file = open('allanturnResp' + str(i) + '.json', 'w')
    file.write(x.text)
    file.close()
