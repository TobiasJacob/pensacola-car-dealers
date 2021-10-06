cd allanturn
rm *.json
python3 allanturnRequest.py
python3 allanturnParse.py
cd ../allstar
# Download json files manually from
# https://www.allstarautoservices.net/inv-scripts/inv/3791058/vehicles?vc=a&f=id%7csn%7cye%7cma%7cmo%7ctr%7cdt%7cta%7ctd%7cen%7cmi%7cdr%7cec%7cic%7cbt%7cpr%7cim%7ceq%7cvd%7cvin%7chpg%7ccpg%7cvc%7cco%7chi%7ccfx%7cacr%7cvt%7ccy%7cdi%7cft%7clo%7ccfk%7ctb%7ccs%7cnop%7cvdf%7cfmi%7cdc&ps=25&pn=0&sb=pr%7cd&sp=n&cb=dws_inventory_listing_5&h=670e54f2bbfe65fa20110c3b0cb30fc6
python3 parse.py
cd ../cardeals
# Save html of view-source:https://cardealsales.com/newandusedcars?clearall=1
python3 parse.py
cd ../hillkelly
# Copy line 5039 of https://www.hillkellydodge.com/inventory/used/, line starting with
# /* <![CDATA[ */
# var pmVlpData = {"tokens": ...}
# use the json object as data.json
python3 parse.py
cd ../mckenziemotors
python3 download.py
python3 parse.py
cd ../petemoore
python3 algoliarequest.py
python3 parse.py
cd ../sandysansing
python3 allanturnRequest.py
python3 allanturnParse.py
