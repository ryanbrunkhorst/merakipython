import requests
import csv

with open("networkids.csv", "r") as a_file:
    for line in a_file:
        networkid = line.strip()
        url = "https://api.meraki.com/api/v0/networks/%s/wireless/rfProfiles" %(networkid)
        payload="{\r\n    \"apBandSettings\": {\r\n        \"bandOperationMode\": \"dual\",\r\n        \"bandSteeringEnabled\": true\r\n    },\r\n    \"twoFourGhzSettings\": {\r\n        \"maxPower\": 15,\r\n        \"minPower\": 6,\r\n        \"minBitrate\": 11,\r\n        \"validAutoChannels\": [1,6,11]\r\n    },\r\n    \"fiveGhzSettings\": {\r\n        \"maxPower\": 24,\r\n        \"minBitrate\": 12,\r\n        \"minPower\": 18,\r\n        \"channelWidth\": \"20\",\r\n        \"validAutoChannels\": [36,40,44,48,149,153,157,161]\r\n    },\r\n    \"bandSelectionType\": \"ap\",\r\n    \"minBitrateType\": \"band\",\r\n    \"name\": \"RFPROFILENAME\",\r\n    \"clientBalancingEnabled\": false\r\n}"
        headers = {
          'Accept': '*/*',
          'Content-Type': 'application/json',
          'X-Cisco-Meraki-API-Key': 'SECRET'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
