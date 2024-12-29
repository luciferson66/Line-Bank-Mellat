import requests
import json

url = "https://ns2.bankmellat.ir/api/resource?api_key=f4e04...................&account=IR83012002............."
headers = {
    "Content-Type": "Json.json",
    "API-KEY": "f4e0457a-9f57-8d6c-8428f8474f3866cf"
    }

data = {
"account_number": "",
"mobile_number": "",
"amount": 220000000000000,
"description": "",

"IN DETITY CODE/SWIFT CODE": "",
"INTERBANK BLOCKING CODE": "",
"SORT CODE": "",
"RELEASE CODE": "",
"ACCESS CODE": "",
"TRANSACTION CODE": "",
"TRANSACTION ID": "",
"FINAL CODE": "",
"TRANSFER CODE": "",
"WTS SERVER": "",
"BONDING KEY": "",
"DOWNLOAD CODE": "",
"RECEIVING CODE": "",
"ACTIVATION CODE": "",
"DEPOSIT TRANSACTION CODE": "",
"WITHDRAWAL CODE": "",
"WITHDRAWAL PASSWORD": "",
"UTR CODE": "",
"ACCEPT CODE": "",

}


response = requests.post(url,headers=headers, data=json.dumps(data))
print(response.text)
