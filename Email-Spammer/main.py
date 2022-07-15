#!/usr/bin/python
from importlib import import_module
from argparse import ArgumentParser
import os
from handlers import *

def destroy(email, fName, lName):
    print(f"Destroying {email}")
    for file in os.listdir('handlers'):
        if file.endswith('.py'):
            try:
                handler = import_module(f'handlers.{file[:-3]}')
                res = handler.send(email, fName, lName)
                if res:
                  print(f"Signed up to {handler.inf()['name']}")
                else:
                  print(f"Failed to sign up to {handler.inf()['name']}")
            except Exception as e:
                print('Error while signing up: ')
                print(e)

def main():
    parser = ArgumentParser(description="TESTING for email spammer")

    parser.add_argument("email",
                        nargs="+", metavar="EMAIL",
                        action="store",
                        help="figure it out"
                        )

    parser.add_argument("--verbose", "-v",
                        action="store_true", dest="verbose", default=False,
                        help="figure it out"
                        )
    args = parser.parse_args()

    willing = input(f"Are you sure you want to destroy {args.email} y/N: ")

    if willing == "y" or willing == "Y":
        destroy(args.email, fName = "Jack", lName = "Doe")


if __name__ == "__main__":
    main()