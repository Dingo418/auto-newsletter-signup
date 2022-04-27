import globals as g

#option 1 = get
#option 2 = post
#option 3 = post + json

data = {
#guardian
0 :	{
  "name" : "guardian",
  "type" : 1,
 	"url" : "https://mc.us10.list-manage.com/subscribe/form-post-json",
  "payload": {
    'u': '7e6df2d1155a77e28a5ba530a',
    'id': '32fd3a6de0',
    'popup': 'true',
    'EMAIL': g.email,
    'FNAME': g.fName,
    'LNAME': g.lName,
    'b_7e6df2d1155a77e28a5ba530a_32fd3a6de0': '',
    'c': 'dojo_request_script_callbacks.dojo_request_script1'},
    'orgData': '{"latitude":-31.9471,"longitude":115.8647,"cont_from_org":"anzo","address_data_from_geolocation":{"area_code":0,"city":"","country_code":"AU","postal_code":"","region_code":"WA"},"org_id":"ped"}'
    },
#peta
1 :	{
  "name" : "peta",
  "type" : 2,
	"url" : "https://www.peta.org.au/wp-admin/admin-ajax.php",
  "payload": {
    'supporter.emailAddress': "testing@icloud.com",
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
    'action': 'ens_submit_subscription_form',}
  },
#scientology
2 :	{
  "name" : "scientology",
  "type" : 2,
	"url" : "https://www.scientology.org.au/form/subscribe.action",
  "payload": {
    'captcha': 'V@3fsasdfasdfAAdgf9J*',
    'reach': 'true',
    'locale': 'en',
    'email': 'jidfj@icloud.com',
    'g-recaptcha-response': '03AGdBq24dyltBgYB5_WR4Bw_qC4fLzBBOd3e9e7ZyUWBg2SzeijIeRdEER_eOI6JoNwIEF1jJ3Q6W_TIZPyx_0EVmHKMgcA6s_0v2HPqfNm6kESxM1jfPDZAnSXiYhHQpcgTs8pR7WscETvo5Z7EI450lt98uFXXDU-r7Yk4KWZn3U9wHgkRMQwX8Q3Uv4-1kw9Yxcl7oJuL20X6PS_wYkQ9unGGQfAlFFcf_KG8prAyciPPohP-3dLraF0LUHcXjrmvlU_Qwo4NzynkTziL2r1XXTgCYTNn-Z9krOtgSrEbft8pTqsMGy2W2tBauF0HtZ2F6J2rHgoZhMsiYTECKpqJOT3-id2SpKEMvnECHqp4TEUG9EslEaOUciVVER_lbcQ9cNJDHmZeNYMCI-rqpIB-_W9YqZb3zP8F1hDjgIq-ZhypVd4NjomIrvp3DPBjvU4AwUqTc_BnRR1vAdYO_Q-fzKCTjMFckRg',}
  },
#abc
3 : {
  "name" : "abc",
  "type" : 3,
  "url"  : 'https://edm.abc-prod.net.au/latest/subscribe',
  
}
}