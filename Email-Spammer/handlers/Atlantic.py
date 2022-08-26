# POST https://accounts-api.theatlantic.com/api/v1/newsletters/sign-up/

# Content-Type: multipart/form-data

# newsletters: One Story to Read Today

# email: example_email@gmail.com


import requests


def inf():

    return { 

        "name": "The Atlantic",

        "url" : "https://www.theatlantic.com/"

    }




def send(email, fName, lName, phone, zip):
    url = "https://accounts-api.theatlantic.com/api/v1/newsletters/sign-up/"

    headers = {
        "Content-Type": "multipart/form-data"
    }

    data = {
        "newsletters": "One Story to Read Today",
        "email": email
    }

    res = requests.post(url, headers=headers)


    return res.ok

