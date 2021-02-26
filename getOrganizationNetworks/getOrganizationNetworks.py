import requests #needed for API request
import json #needed to convert REST API response to json
import csv #needed for creating CSV
    
url = "https://api.meraki.com/api/v0/organizations/organizationId/networks" #must change the organization id

payload={}
headers = {
  'Accept': '*/*',
  'X-Cisco-Meraki-API-Key': 'SECRET'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text) #uncomment to print entire REST API response
json = response.json() #converts REST API response to json for parsing

#Loops through json and prints name and id for each network
#Also adds name and id to a CSV named networks.csv

with open('networks.csv', 'w', newline='') as networks:
    networks_writer = csv.writer(networks, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    networks_writer.writerow(['NAME', 'ID'])  #Creates the columns for the CSV
    for site in json:
        print(site["name"]) #prints name field
        print(site["id"]) #prints id field
        networks_writer.writerow([site["name"], site["id"]]) #adds a new line to the CSV for each site and appends name/id fields






