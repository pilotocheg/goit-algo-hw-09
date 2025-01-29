def find_min_coins(sum):
    coins = [50, 25, 10, 5, 2, 1]
    result = {coin: 0 for coin in coins}

    dp = [float("inf")] * (sum + 1)
    dp[0] = 0
    coin_used = [0] * (sum + 1)

    for coin in coins:
        for i in range(coin, sum + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    while sum > 0:
        coin = coin_used[sum]
        if coin != 0:
            result[coin] += 1
        sum -= coin

    return result
