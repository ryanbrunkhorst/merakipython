import requests
import csv

with open('rfprofiles.csv', 'w', newline='') as rf: # 'w' will overwrite any existing file named rfprofiles.csv
    rf_writer = csv.writer(rf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    rf_writer.writerow([
        'networkid',
        'name',
        'clientBalancing',
        'minBitrateType',
        'bandSelType',
        'bandOPMode',
        'bandSteering',
        '2.4 min power',
        '2.4 max power',
        '2.4 min datarate',
        '2.4 autochannels',
        '5 min power',
        '5 max power',
        '5 min datarate',
        '5 autochannels',
        '5 channelwidth'
        ])  #Creates the columns for the CSV

with open("networkids.csv", "r") as a_file:
    for line in a_file:
        networkid = line.strip()
        url = "https://api.meraki.com/api/v0/networks/%s/wireless/rfProfiles" %(networkid)

        payload={}
        headers = {
          'Accept': '*/*',
          'X-Cisco-Meraki-API-Key': 'SECRET'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        #print(response.text)
        json = response.json() #converts REST API response to json for parsing

        with open('rfprofiles.csv', 'a', newline='') as rf: # 'a' will only append to the rfprofiles.csv file
            rf_writer = csv.writer(rf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #rf_writer.writerow(['networkid','rf number', 'name', 'enabled', 'authmode'])  #Creates the columns for the CSV
            #print(networkid)
            for rf in json:
                print(rf["networkId"]) #prints rf number field
                print(rf["name"]) #prints RF profile name
                #print(rf["minBitrateType"]) 
                #print(rf["apBandSettings"]["bandOperationMode"])
                rf_writer.writerow([
                    networkid,
                    rf["name"],
                    rf["clientBalancingEnabled"],
                    rf["minBitrateType"],
                    rf["bandSelectionType"],
                    rf["apBandSettings"]["bandOperationMode"],
                    rf["apBandSettings"]["bandSteeringEnabled"],
                    rf["twoFourGhzSettings"]["minPower"],
                    rf["twoFourGhzSettings"]["maxPower"],
                    rf["twoFourGhzSettings"]["minBitrate"],
                    rf["twoFourGhzSettings"]["validAutoChannels"],
                    rf["fiveGhzSettings"]["minPower"],
                    rf["fiveGhzSettings"]["maxPower"],
                    rf["fiveGhzSettings"]["minBitrate"],
                    rf["fiveGhzSettings"]["validAutoChannels"],
                    rf["fiveGhzSettings"]["channelWidth"]
                    ]) #adds a new line to the CSV for each rf and appends name/id fields
                
