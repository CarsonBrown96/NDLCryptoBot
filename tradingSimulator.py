prices = #array of prices
previous_count = #split of historical data and what we later use to test
position = #tuple (coins owned, money spent on those coins)
money = #used to track profit/loss

def simulate():
    for i in prices[previous:]:
        decision = evaluate(prices[:previous])
        money += decision[1]
        previous += 1
    return money + (position[0] * prices[-1])

def evaluate(previous_data):
    #takes an array of previous prices
    #RETURNS: tuple of (coins exchanged, investment)
    #A buy will be a negative investment, a sell will be a positive investment

def __main__:
    simulate()
