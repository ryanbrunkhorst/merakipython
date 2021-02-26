import requests
#you must replace networkId
url = "https://api.meraki.com/api/v0/networks/networkId/switch/accessControlLists" 

payload="{\r\n  \"rules\": [\r\n    {\r\n\
\
\"comment\": \"DenySSH\",\r\n\
\"policy\": \"deny\",\r\n\
\"ipVersion\": \"ipv4\",\r\n\
\"protocol\": \"tcp\",\r\n\
\"srcCidr\": \"10.1.10.2/32\",\r\n\
\"srcPort\": \"any\",\r\n\
\"dstCidr\": \"172.16.30.5/32\",\r\n\
\"dstPort\": \"22\",\r\n\
\"vlan\": \"10\"\r\n\
},\r\n    {\r\n\
\
\"comment\": \"Allow Server Access\",\r\n\
\"policy\": \"Allow\",\r\n\
\"ipVersion\": \"ipv4\",\r\n\
\"protocol\": \"tcp\",\r\n\
\"srcCidr\": \"10.1.10.2/32\",\r\n\
\"srcPort\": \"any\",\r\n\
\"dstCidr\": \"192.168.76.0/24\",\r\n\
\"dstPort\": \"any\",\r\n\
\"vlan\": \"10\"\r\n\
},\r\n    {\r\n\
\
\"comment\": \"Deny 172 RFC1918\",\r\n\
\"policy\": \"deny\",\r\n\
\"ipVersion\": \"ipv4\",\r\n\
\"protocol\": \"tcp\",\r\n\
\"srcCidr\": \"any\",\r\n\
\"srcPort\": \"any\",\r\n\
\"dstCidr\": \"172.16.0.0/12\",\r\n\
\"dstPort\": \"any\",\r\n\
\"vlan\": \"10\"\r\n\
}\r\n  ]\r\n\
\
}"

# Last Access Control Entry must be }". All except the last entry must have a comma after

headers = {
  'Accept': '*/*',
  'Content-Type': 'application/json',
  'X-Cisco-Meraki-API-Key': 'SECRET'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
