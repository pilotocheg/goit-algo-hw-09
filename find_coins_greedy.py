def find_coins_greedy(sum):
    coins = [50, 25, 10, 5, 2, 1]
    result = {coin: 0 for coin in coins}

    for coin in coins:
        while sum >= coin:
            sum -= coin
            result[coin] += 1

    return result
