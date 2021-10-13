def birthdayCakeCandles(candles):
    # Write your code here

    larger_candle = candles[0]
    for i in range(len(candles)):
        if larger_candle < candles[i]:
            larger_candle = candles[i]
    return candles.count(larger_candle)


if __name__ == '__main__':
    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)
