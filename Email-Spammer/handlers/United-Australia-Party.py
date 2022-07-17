import requests

def inf():
    return { 
        "name": "United Australia Party",
        "url" : "https://www.unitedaustraliaparty.org.au/"
    }



def send(email, fName, lName, phone, zip):
    burp0_url = f"https://maillist-manage.com:443/weboptin.zc?CONTACT_EMAIL={email}&LASTNAME={fName} {lName}&SIGNUP_SUBMIT_BUTTON=Join%20Now&submitType=optinCustomView&formType=QuickForm&zx=1279d334f&zcvers=3.0&mode=OptinCreateView&zcld=162781fa37f76f09&zc_trackCode=ZCFORMVIEW&zc_formIx=3z78eb5cb9d73aa10102c1c42523c03667f90ef74acaaceb2f846182521d196340&lf=1658029307363&di=114323221037174798701658029307363&responseMode=inline&sourceURL=https%3A%2F%2Fwww.unitedaustraliaparty.org.au%2F&tpIx=3zab4eb9b93ad704226143028e9178bd1c0752e5bfc01c59c26bdea4baf320de99&custIx=3zab4eb9b93ad704226143028e9178bd1c5f81566cc2d16d3866e0c778188bbd7b"
    burp0_headers = {
        "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Accept": "*/*",
        "Origin": "https://www.unitedaustraliaparty.org.au",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.unitedaustraliaparty.org.au/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "close"
    }
    res = requests.post(burp0_url, headers=burp0_headers)

    return res.ok
