import requests

def inf():
    return { 
        "name": "BBC",
        "url" : "https://www.peta.org/"
    }



def send(email, fName, lName, phone, zip):
    burp0_url = f"https://pages.s6.exacttarget.com:443/page.aspx?QS=2e4c31a3756cb9409d0c1f0ca0648049d308038c42672a72ad1393481591df3a&svc=100194&email{email}&country=US&marketingagreed=Y"
    burp0_headers = {
    "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\"",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/json charset=utf-8",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://pages.s6.exacttarget.com/page.aspx?QS=2e4c31a3756cb9408def46c8281c827b606a8ae434b39be8271057e45e2d1bcc",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Connection": "close"
}    
    res = requests.get(burp0_url, headers=burp0_headers)
    return res.ok
