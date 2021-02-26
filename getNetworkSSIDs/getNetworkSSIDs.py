# This script will iterate through multiple networks retrieving all SSIDs and exporting to a CSV for review
# It will list the networkid, SSID number, SSID name, whether the SSID is active, and what authentication is used
# If a network id does not have wireless, then this script will fail


import requests #needed for API request
import json #needed to convert REST API response to json
import csv #needed for creating/reading CSV


with open('ssids.csv', 'w', newline='') as ssid: # 'w' will overwrite any existing file named ssids.csv
    ssid_writer = csv.writer(ssid, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    ssid_writer.writerow([
        'networkid',
        'ssid number',
        'name',
        'enabled',
        'authmode',
        'ipAssignmentMode'
        ])
    #Creates the columns for the CSV

with open("networkids.csv", "r") as a_file: #loops through each networkid in the networkids.csv and calls Meraki REST API
    for line in a_file:
        networkid = line.strip() #sets networkid variable from CSV
        url = "https://api.meraki.com/api/v0/networks/%s/ssids" %(networkid)
        payload={}
        headers = {
          'Accept': '*/*',
          'X-Cisco-Meraki-API-Key': 'SECRET'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        #print(response.text) #commented out since it outputs all text from response
        json = response.json() #converts REST API response to json for parsing

        with open('ssids.csv', 'a', newline='') as ssid: # 'a' will only append to the ssids.csv file
            ssid_writer = csv.writer(ssid, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #ssid_writer.writerow(['networkid','ssid number', 'name', 'enabled', 'authmode'])  #Creates the columns for the CSV
            print(networkid)
            for ssid in json:
                print(ssid["number"]) #prints ssid number field
                print(ssid["name"]) #prints name field
                print(ssid["enabled"]) #prints enabled field
                print(ssid["authMode"]) #prints enabled field
                ssid_writer.writerow([
                    networkid,
                    ssid["number"],
                    ssid["name"],
                    ssid["enabled"],
                    ssid["authMode"],
                    ssid["ipAssignmentMode"],
                    ])
                #adds a new line to the CSV for each ssid and appends name/id fields
                







