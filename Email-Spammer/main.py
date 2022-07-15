#!/usr/bin/python
import requests
from argparse import ArgumentParser
from handlers import *

def destroy(email, fName, lName):
    print(f"Destroying {email}")
    guardian.send(email, fName, lName)
    peta.send(email, fName, lName)
    

    

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