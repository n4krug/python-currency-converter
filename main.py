import requests
import json
import sys


# Global DEFs
with open('OE_APP_ID', 'r')as f:
    OE_APP_ID = f.read()


# Get latest currency data from openexchangerates
def get_rates(base):
    
    params = {
        "app_id": OE_APP_ID,
        "base": base
    }

    currencies = requests.get(f"https://openexchangerates.org/api/latest.json", params).json()

    rates = currencies["rates"]

    return rates


def help():
    print("Usage: main.py <from-currency> <from-amount> <to-currency>")
    print("Example: main.py USD 100 EUR")


def get_args():
    args = sys.argv[1:]

    if args[0] == "-h" or args[0] == "--help" or len(args) != 3:
        help()

    return args


def main():

    args = get_args()

    base = args[0]

    in_amount = args[1]

    out_currency = args[2]

    rates = get_rates(base)