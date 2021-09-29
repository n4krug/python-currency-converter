import requests
import json
import sys

OE_APP_ID = ""

# Global DEFs
with open("OE_APP_ID", "r") as f:
    OE_APP_ID = f.read()


# Get latest currency data from openexchangerates
def get_rates(base):

    params = {"app_id": OE_APP_ID, "base": base}

    currencies = requests.get(
        f"https://openexchangerates.org/api/latest.json", params
    ).json()

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

    in_amount = int(args[1])

    out_currency = args[2]

    rates = get_rates("USD")

    amount_USD = round(in_amount / rates[base], 2)

    amount_out = round(amount_USD * rates[out_currency], 2)

    print(f"{in_amount} {base}")
    print(f"{amount_USD} USD")
    print(f"{amount_out} {out_currency}")


if __name__ == "__main__":
    main()
