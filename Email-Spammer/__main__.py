#! /usr/bin/env python3

"""
Email-Spammer: Add emails across multiple newsletter services
This module contains the main logic to add emails to 
"""

import sys


if __name__ == "__main__":
    # Check if the user is using the correct version of Python
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 6):
        print("Spammer requires Python 3.10+\nYou are using Python %s, which is not supported by Spammer" % (python_version))
        sys.exit(1)

    import spammer
    spammer.main()