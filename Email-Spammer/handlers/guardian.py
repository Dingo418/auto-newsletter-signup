import requests
def send(email, fName, lName):
    url = "https://mc.us10.list-manage.com/subscribe/form-post-json"
    payload = {
        'u': '7e6df2d1155a77e28a5ba530a',
        'id': '32fd3a6de0',
        'popup': 'true',
        'EMAIL': email,
        'FNAME': fName,
        'LNAME': lName,
        'b_7e6df2d1155a77e28a5ba530a_32fd3a6de0': '',
        'c': 'dojo_request_script_callbacks.dojo_request_script1',
    }
    push = requests.get(url=url, params=payload)
    print(f"{email} was succesfully subscribed to guardian Newsletter")
#    print(push.text)