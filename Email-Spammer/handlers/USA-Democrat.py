import requests
def inf():
    return { 
        "name": "USA Democratic Party",
        "url" : "https://democrats.org/"
    }



def send(email, fName, lName, phone, zip):
    
    burp0_url = "https://actionnetwork.org:443/api/v2/forms/4f51c8cc-384d-435b-ae17-865695e8b5e8/submissions"
    burp0_headers = {
        "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="96"',
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Origin": "https://democrats.org",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://democrats.org/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    }
    burp0_json = {
        "person": {
            "email_addresses": [{"address": email, "status": "subscribed"}],
            "phone_numbers": [{"number": phone, "status": "subscribed"}],
            "postal_addresses": [{"postal_code": zip}],
        },
        "triggers": {"autoresponse": {"enabled": True}},
    }
    res = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)

    return res.ok
