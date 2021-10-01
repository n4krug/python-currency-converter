import requests


class CurrencyConverter:
    def __init__(self, app_id):
        self.app_id = app_id

    # Get latest currency data from openexchangerates
    def get_rates(self, base="USD"):

        params = {"app_id": self.app_id, "base": base}

        currencies = requests.get(
            f"https://openexchangerates.org/api/latest.json", params
        ).json()

        rates = currencies["rates"]

        return rates

    def convert_currencies(
        self, rates, in_amount, in_currency="USD", out_currency="EUR"
    ):
        USD_amount = round(in_amount / rates[in_currency], 2)

        out_amount = round(USD_amount * rates[out_currency], 2)

        return out_amount


OE_APP_ID = ""

# Global DEFs
with open("OE_APP_ID", "r") as f:
    OE_APP_ID = f.read()


def help():
    print("Usage: main.py <from-currency> <from-amount> <to-currency>")
    print("Example: main.py USD 100 EUR")


def get_args():
    import sys

    args = sys.argv[1:]

    if args[0] == "-h" or args[0] == "--help" or len(args) != 3:
        help()

    return args


def main():

    c_converter = CurrencyConverter(OE_APP_ID)

    args = get_args()

    base = args[0]

    in_amount = int(args[1])

    out_currency = args[2]

    rates = c_converter.get_rates("USD")

    amount_out = c_converter.convert_currencies(rates, in_amount, base, out_currency)

    print(f"{in_amount} {base}")
    print(f"{amount_out} {out_currency}")


if __name__ == "__main__":
    main()
