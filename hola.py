"""
In this project, you'll create a program that that tells
you when the value of your Bitcoin falls below $30,000.
You will need to:
- Create a function to convert Bitcoin to €
- If your Bitcoin falls below 30,000€ print a message.
You can assume that 1 Bitcoin is worth 40,000€
===> You've redeemed a hint. Replace the _'s with code to complete
this exercise.
"""
investment_in_bitcoin = 1.2
bitcoin_to_euros = 20000
# 1) write a function to calculate bitcoin to euros
def bitcoinToEuros(investment_in_bitcoin,bitcoin_to_euros):
    usd_value = investment_in_bitcoin * bitcoin_to_euros
    return usd_value


investment_in_usd = bitcoinToEuros(investment_in_bitcoin, bitcoin_to_euros)
if investment_in_usd <= 30000:
    print("Investment below 30,000€! SELL!")
else:
    print("Investment above 30,000€")