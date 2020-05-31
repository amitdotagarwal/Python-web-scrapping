


# Request object to call Grofers API
import requests
# To convert data into json
import json
# For Read and write operation
import io

# Created a emty file and initialize headers with UTF8 encoding
with io.open("grofers.csv", "w", encoding='utf8') as f1:
	f1.write("ITEMNAME, MRP, OFFER,RATING\n")
	f1.close()

#Mandatory headers for the Grofers API
headers = {
    'app_client': 'consumer_web',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': '*/*'
}

# Parsns to fetch data
params = (
    ('l0_cat', '16'),
    ('start', '0'),
    ('next', '48'),
)

print("Webscraping started")

# API calling
response = requests.get('https://grofers.com/v4/search/merchants/26015/products/', headers=headers, params=params)

# Convert into JSON object
json_response = json.loads(response.text)["result"]["products"]
for i in range(len(json_response)):
	variant_info= json_response[i]["variant_info"]
	for j in range(len(variant_info)):
		name= variant_info[j]["line_1"]
		mrp=variant_info[j]["mrp"]
		offer = variant_info[j]["sbc_offer"]
		rating=  variant_info[j]["rating"]
		datastring= str(name)+ "," + str(mrp) + "," + str(offer)+ "," + str(rating) + '\n'
# Amend data in the excel sheet
		with io.open("grofers.csv", "a", encoding="utf8") as f1:
			f1.write(datastring)
			f1.close()
print("Webscraping completed")
