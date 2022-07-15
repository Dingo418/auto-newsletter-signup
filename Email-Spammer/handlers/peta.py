import requests
def inf():
    return {
        "name": "PETA"
    }

def send(email, fName, lName):
    url = "https://www.peta.org.au/wp-admin/admin-ajax.php"
    payload = {
        'supporter.emailAddress': email,
        'img_bt': '',
        'supporter.questions.130956': 'Y',
        'ens_id': '18086',
        'post_id': '4',
        'pma_subscription_form_title': 'Sign Up for E-Mail Updates',
        'ga_label': 'Home Page: AU Home Page E-Mail Opt-In Form',
        'w_post_id': '4',
        'country_detected': 'AU',
        'locale': 'en',
        'wpml_lang': 'en',
        'layout': 'shortcode',
        'en_txn6': 'https%3A%2F%2Fwww.peta.org.au%2F',
        'pma_template': 'subscription_form',
        'action': 'ens_submit_subscription_form'
    }
    res = requests.post(url=url, params=payload)
    return res.ok
    
        