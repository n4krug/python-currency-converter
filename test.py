from main import CurrencyConverter

with open("OE_APP_ID", "r") as f:
    OE_APP_ID = f.read()

cc = CurrencyConverter(OE_APP_ID)

rates = cc.get_rates()
print(rates)

print(cc.convert_currencies(rates, 100, "YEN", "EUR"))
