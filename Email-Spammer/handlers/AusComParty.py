import requests

def inf():
    return { 
        "name": "Australian Comunmist Party",
        "url" : "https://auscp.org.au/"
    }



def send(email, fName, lName, phone):
    burp0_url = (
        "https://auscp.org.au:443/wp-json/contact-form-7/v1/contact-forms/55/feedback"
    )
    burp0_cookies = {
        "chaport-60c06ea0f2841d1068af5e84": "2ecb5f32-d46b-499f-b7c1-792e746c625c/cdV9ZtOPkdD6jwALUBQbbdb8KtboPRaI34i",
        "cf7pp_amount_total": "0.00",
        "cf7pp_stripe_state": "live",
        "cf7pp_payment_id": "4367",
    }
    burp0_headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Accept": "application/json, */*;q=0.1",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://auscp.org.au/",
        "Content-Type": "multipart/form-data; boundary=---------------------------179962607429440171881674225122",
        "Origin": "https://auscp.org.au",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Te": "trailers",
        "Connection": "close",
    }
    burp0_data = f'-----------------------------179962607429440171881674225122\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n55\r\n-----------------------------179962607429440171881674225122\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.6\r\n-----------------------------179962607429440171881674225122\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nen_US\r\n-----------------------------179962607429440171881674225122\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f55-p6-o1\r\n-----------------------------179962607429440171881674225122\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n6\r\n-----------------------------179962607429440171881674225122\r\nContent-Disposition: form-data; name="_wpcf7_posted_data_hash"\r\n\r\n9e2fd9934c2016b165b949119459c0ff\r\n-----------------------------179962607429440171881674225122\r\nContent-Disposition: form-data; name="email-214"\r\n\r\n{email}\r\n-----------------------------179962607429440171881674225122--\r\n'
    res = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    return res.ok
