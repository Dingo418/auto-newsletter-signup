#! /usr/bin/env python3
from importlib import import_module
from argparse import ArgumentParser
from colorama import Fore, Style
import os
neutral = f"{Fore.WHITE}[{Fore.YELLOW + Style.BRIGHT}*{Fore.WHITE}]"
negative = f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}]"
postive = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]"


def destroy(email, fName, lName, phone, zip, verbose, amount):
    for file in os.listdir('handlers'):
        if file.endswith('.py'):
            try:
                handler = import_module(f'handlers.{file[:-3]}')
                res = handler.send(email, fName, lName, phone, zip)
                if res:
                  print(f"{postive + Fore.GREEN} {handler.inf()['name']}: {Fore.WHITE}Subscribed Sucessfully!")
                else:
                  print(f"{negative + Fore.GREEN} {handler.inf()['name']}: {Fore.WHITE}Failed")
            except Exception as e:
                print(f'{negative} Error while signing up to the {file}: ')
                print(e)

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
                        action="store", default="Jack-Doe",
                        help="The name of the target. Place a hyphen inbetween the first and last name for example Jack-Doe"
                        )


    parser.add_argument("-p","--phone",
                        action="store", default="555 555 1234",
                        help="The targets phone number you want to link"          
    )

    parser.add_argument("-z", "--zip",
                        action="store", default="21443",
                        help="The target's zip code")
    
    parser.add_argument("-r", "--repeat",
                        action="store", default=1, type=int,
                        help="The amount of times you want the script to repeat"
                        )

    parser.add_argument("-a", "--amount",
                        action="store",default=float('inf'),
                        help="The amount of times"
                        )


    args = parser.parse_args()
    try:
        fName,lName = args.name[:].split("-")
    except ValueError:
        print("Error: The name is larger then two words. Please try again with less words.")
        exit()
        
    willing = input(f"{neutral + Fore.GREEN} Are you sure you want to destroy {Fore.WHITE}{args.email}{Fore.GREEN} y/N: {Fore.WHITE}")

    if willing == "y" or willing == "Y":
        for email in args.email:
            print(f"{neutral + Fore.GREEN} Destroying {Fore.WHITE}{email}")
            for _ in range(0,args.repeat):
                destroy(email, fName, lName, args.phone, args.zip, args.verbose, args.amount)
            print(f"{neutral} {email + Fore.GREEN} has been destroyed!")                
            



if __name__ == "__main__":
    main()