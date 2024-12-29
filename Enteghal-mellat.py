import json
import hashlib
import hmac
import requests


ip_address = "176.56.156.22:443"
digitalSignType = "3"
payeeAccNo = ""
payeeExtAccNo =	""
payer_account_number =	""
payer_external_account_number = ""
payerId = "148"
sourceCardType = "0"
targetCardType = "0"
totalTransferredAmount = "0"
transferAmount = "30000000000000"
transferDesc = 	""
destination_account_api_key = "f4e0457a-9f57-8................."
header = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMD..........................uIiwiZXhwIjoxNzE5O...................E3MTk5MTU1Nzh9.dZo.......................sq-fotTBW..............Z_8q0lradi2_......................_G6qpAFZ7Hlw"
destination_account_id = "228600804"
destination_account_url = "https://ebanking.bankmellat.ir/ebanking/mib/mellatDraftConfirm"


# اطلاعات حساب مبدا
#source_account_ip = "176.56.156.137"
#source_account_number = ""
#source_account_shaba = "IR91012.........."
#source_account_amount = 30000000000000
#source_account_name = "Esme Hesab Mabda"
#Source_account_TRANSACTION_CODE = ""
#source_account_Access_code = ""
#source_account_FINAL_BLOCKING_CODE = ""
#source_account_TRANSFER_CODE = ""
#source_account_UTR = ""
#source_account_RELEASE_CODE = ""


# اطلاعات حساب مقصد
#destination_account_api_key = "f4e0457a-9f5....................."
#destination_account_url = "https://bpm.shaparak.ir/pgwchannel/startpay.mellat?f4e04.............................74f3866cf=P65.............................."
#destination_account_ip = "176.56.156.136"
#destination_account_shaba = "IR91......................."
#destination_account_number = ""
#destination_account_id = ""
#destination_account_transfer_id = ""

def convert_to_RIALS(amount):
    return amount * 30000000000000

# تولید payload برای ارسال به سرویس مقصد
payload = {
    "api_key": destination_account_api_key,
    "Bearer": header,
    "account_number": payeeAccNo,
    "payerId": payerId,
    "id": destination_account_id,
    "amount": convert_to_RIALS(transferAmount)
}

# تولید CRC
def generate_crc(key, message):
    return hmac.new(key.encode(), str(message).encode(), hashlib.sha256).hexdigest()

# تولید HMAC با الگوریتم HUB10
def generate_hmac(key, message):
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

# افزودن CRC و HMAC به payload
payload["crc"] = generate_crc(ip_address, json.dumps(payload))
payload["hmac"] = generate_hmac(destination_account_api_key, json.dumps(payload))
payload["response_url"] = "https://ebanking.bankmellat.ir/ebanking/mib/mellatDraftConfirm/response"
payload["acknowledge_url"] = "https://ebanking.bankmellat.ir/ebanking/mib/mellatDraftConfirm/acknowledge"

# ارسال درخواست به سرویس مقصد
response = requests.post(destination_account_url, json=payload)



destination_account_api_key = "f4e04......................................"

hmac_value = generate_hmac(destination_account_api_key, json.dumps(payload))
print("HMAC:", hmac_value)
# بررسی و پردازش پاسخ
if response.status_code == 200:
    print("انتقال پول با موفقیت انجام شد.")
else:
    print("خطا در انتقال پول.")



# در این ماژول مراحل انتقال پول انجام خواهد شد. نکته این هستش که این ماژول ها بعد از ورود از طریق ترمینال و سوییچ بر روی پنل اصلی زیرساخت شبکه بانکی ممکن می باشد. کد HMAC تولید شده بعد از تراکنش قابل بررسی و پیگیری در شبکه بانکی می باشد . همچنین این کد بر اساس اطلاعات وارد شده توسط شما تولید می شود و اگر اطلاعات وارد شده توسط شما درست نباشند, کد تولید شده در شبکه بانکی و سوییف غیر قابل استفاده خواهد بود. 
