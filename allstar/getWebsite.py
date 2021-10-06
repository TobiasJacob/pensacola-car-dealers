import requests

urls = ['https://www.allstarautoservices.net/inv-scripts/inv/3791058/vehicles?vc=a&f=id%7csn%7cye%7cma%7cmo%7ctr%7cdt%7cta%7ctd%7cen%7cmi%7cdr%7cec%7cic%7cbt%7cpr%7cde%7cim%7ceq%7cvd%7cvin%7chpg%7ccpg%7cvc%7cco%7chi%7ccfx%7cacr%7cvt%7ccy%7cdi%7cft%7clo%7ccfk%7ctb%7ccs%7cvdf%7cfmi%7cdc&ps=25&pn=0&sb=pr%7cd&sp=n&cb=dws_inventory_listing_2&h=22738237db67d109f6d5677809929cac',
        'https://www.allstarautoservices.net/inv-scripts/inv/3791058/vehicles?vc=a&f=id%7csn%7cye%7cma%7cmo%7ctr%7cdt%7cta%7ctd%7cen%7cmi%7cdr%7cec%7cic%7cbt%7cpr%7cde%7cim%7ceq%7cvd%7cvin%7chpg%7ccpg%7cvc%7cco%7chi%7ccfx%7cacr%7cvt%7ccy%7cdi%7cft%7clo%7ccfk%7ctb%7ccs%7cvdf%7cfmi%7cdc&ps=25&pn=1&sb=pr%7cd&sp=n&cb=dws_inventory_listing_2&h=32fd6f131d710b749c09785c41e3d826']

cookies = {'__cfduid': 'd83dae87341b53e59de56f22728ef03881599698302',
           'cid': '90214fa8ee454a1982c0c2f59b1dfd28',
           'dws-recent-vehicles': '["197155"]',
           '__cf_bm': '8a792f626850e8712c184b2de2368eec13c50afc-1601330110-1800-AQZDckOXivEeHXVcl86PANGuFuLVnkC2+8/tMrvo3xQxYgDjy6kLSLn40ZXsH2yjcjoCRl36nHkkKgBwAGpz1xQ=',
           'sid': 'efe5eab1677446ecb7834528d5413de7',
           'sidts': '-8586002762193644068',
           'dws-inv-back-page': 'https://www.allstarautoservices.net/inventory/?page_no=1&pager=25'}

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

for i in range(2):
    print(i)
    x = requests.get(urls[i], cookies=cookies, headers=headers)
    file = open('allstar' + str(i) + '.json', 'w')
    file.write(x.text)
    file.close()
