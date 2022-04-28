from email import header
import requests
import json
import database as d
import globals as g

peta_header = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-length': '398',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': '_ga=GA1.3.1698909609.1651065026; _gid=GA1.3.471045418.1651065026; BE_CLA3=p_id%3DLRL48AN4ARN4RJN4RLNRA4AR8AAAAAAAAH%26bf%3De5c87ef40a376f6e94dc650818219414%26bn%3D1%26bv%3D3.44%26s_expire%3D1651151426717%26s_id%3DLRL48AN4ARN4RLARN82RA4AR8AAAAAAAAH; _gat=1; _fbp=fb.2.1651065027060.1585457546; clientLocation=AU; _gali=pma-submit; ens_form_autofill=%7B%7D',
    'origin': 'https://www.peta.org.au',
    'referer': 'https://www.peta.org.au/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


def main():
    data = d.data[1]
    print("type 2")
    push = requests.post(url=data.get("url"), data=data.get("payload"), headers=peta_header)
    print(push.text)
    print(f"{g.email} was succesfully subscribed to {data.get('name')} Newsletter")
    print(push.headers)



if __name__ == "__main__":
    main()