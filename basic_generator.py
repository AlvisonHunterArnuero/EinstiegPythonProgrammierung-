# Made with ❤️ in Python 3 by Alvison Hunter - December 22nd, 2020
xmas_budget = 1000
xmas_gift_dict = {"Apple AirPods":"169.85","Instant Pot":"71.99","Kindle Paperwhite":"119.99","Fitbit Charge 3 ":"118.95","Echo Show 5 ":"59.99","Sony Noise-Canceling Headphones ":"278.99"}
def budget_balance():
    global xmas_budget
    value = None
    while True:
        # Received the sent value
        value = yield xmas_budget
        if value is None: break
        # Substract the value sent from the current xmas_budget variable
        print("-"*50) # To embellish the output only
        xmas_budget -= value

# Let us create the generator object, will you?
gen_remaining = budget_balance()
try:
    print("-"*50) # To embellish the output only
    print("ITEMS".ljust(40," ")+"PRICE")
    print("-"*50) # To embellish the output only
    # Advance until the first "yield"
    next(gen_remaining)      # sending zero values
    for k, v in xmas_gift_dict.items():
        print(f"{k.ljust(40,' ')}${v}")
        gen_remaining.send(float(v))

    next(gen_remaining)      # StopIteration raises here
except StopIteration:
       print("Generator iteration successfully completed.")




