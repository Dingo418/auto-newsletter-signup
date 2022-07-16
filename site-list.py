from importlib import import_module
import os

with open("sites.md", "w") as sites_file:
    sites_file.write('## List of supported urls\n')
    for file in os.listdir('Email-Spammer/handlers'):
        if file.endswith('.py'):
            website = import_module(f'Email-Spammer.handlers.{file[:-3]}')
            info = website.inf()
            sites_file.write(f"1. [{info['name']}]({info['url']})\n")


