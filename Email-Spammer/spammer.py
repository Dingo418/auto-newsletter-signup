#! /usr/bin/env python3
from importlib import import_module
from argparse import ArgumentParser
import os

def destroy(email, fName, lName, phone, verbose):
    print(f"[/] Destroying {email}")
    for file in os.listdir('handlers'):
        if file.endswith('.py'):
            try:
                handler = import_module(f'handlers.{file[:-3]}')
                res = handler.send(email, fName, lName, phone)
                if res:
                  print(f"[+] Signed up to {handler.inf()['name']}")
                else:
                  print(f"[-] Failed to sign up to {handler.inf()['name']}")
            except Exception as e:
                print('Error while signing up: ')
                print(e)
    print(f"[/] {email} has been destroyed")

def main():
    fName, lName = "", ""
    parser = ArgumentParser(description="TESTING for email spammer")

    parser.add_argument("email",
                        nargs="+", metavar="EMAIL",
                        action="store",
                        help="The target email you want to destory"
                        )

    parser.add_argument("-v","--verbose", 
                        action="store_true", default=False,
                        help="Enables verbose"
                        )

    parser.add_argument("-n", "--name",
                        action="store",
                        default="Jack-Doe",
                        help="The name of the target. Place a hyphen inbetween the first and last name for example Jack-Doe"
                        )


    parser.add_argument("-p","--phone",
                        action="store",

                        help="The targets phone number you want to link"
                        
    )

    args = parser.parse_args()
    try:
        fName,lName = args.name[:].split("-")
    except ValueError:
        print("Error: The name is larger then two words. Please try again with less words.")
        exit()
        
    willing = input(f"[/] Are you sure you want to destroy {args.email} y/N: ")

    if willing == "y" or willing == "Y":
        for email in args.email:
            destroy(email, fName, lName, args.phone, args.verbose)



if __name__ == "__main__":
    main()