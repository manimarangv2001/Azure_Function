import requests
import os



def get_catalog_item():
    url = 'https://hexawaretechnologiesincdemo8.service-now.com/api/now/table/sc_cat_item?sysparm_limit=1'

    user = os.environ["SERVICENOW_USERNAME"]
    pwd = os.environ["SERVICENOW_PASSWORD"]

    headers = {"Content-Type":"application/json","Accept":"application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers )
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
    data = response.json()
    return data