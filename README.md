# auto newsletter signup
Python program that auto signs up a given email to a bunch of newsletter services

## flags
```
usage: spammer.py [-h] [-v] [-n NAME] [-p PHONE] [-z ZIP] [-r REPEAT] [-a AMOUNT] EMAIL [EMAIL ...]

TESTING for email spammer

positional arguments:
  EMAIL                 The target email you want to destory

options:
  -h, --help            show this help message and exit
  -v, --verbose         Enables verbose
  -n NAME, --name NAME  The name of the target. Place a hyphen inbetween the first and last name for example Jack-Doe
  -p PHONE, --phone PHONE
                        The targets phone number you want to link
  -z ZIP, --zip ZIP     The target's zip code
  -r REPEAT, --repeat REPEAT
                        The amount of times you want the script to repeat
  -a AMOUNT, --amount AMOUNT
                        The amount of times
```
## Contributing
Go to Contributing.md.

## To do

- [x] Get base code working
- [x] Add more functionality in
- [x] Add colour
- [ ] Add more newsletters
- [ ] Add proxy and tor flag
- [ ] Extract a list of emails from a txt file