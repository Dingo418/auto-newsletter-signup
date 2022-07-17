import requests

def inf():
    return { 
        "name": "PETA-Newsletter",
        "url" : "https://www.peta.org/"
    }



def send(email, fName, lName, phone, zip):
    burp0_url = "https://www.peta.org:443/wp-admin/admin-ajax.php"
    burp0_headers = {
        "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\"",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Origin": "https://www.peta.org",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.peta.org/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "close"
    }
    burp0_data = {
        "supporter.emailAddress": email,
        "img_bt": '',
        "supporter.questions.164": "Y",
        "supporter.questions.167": "Y",
        "ens_id": "5806",
        "post_id": "8",
        "pma_subscription_form_title": "Sign Up for E-Mail",
        "ga_label": "Homepage Top E-News Form",
        "w_post_id": "8",
        "country_detected": "AU",
        "locale": "en",
        "wpml_lang": "en",
        "layout": "shortcode",
        "en_txn6": "https%3A%2F%2Fwww.peta.org%2F",
        "pma_template": "subscription_form",
        "action": "ens_submit_subscription_form"
    }    
    res = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)

    return res.ok
