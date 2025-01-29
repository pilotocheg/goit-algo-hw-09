import timeit
from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins

sum = 10**7


def test_performance(fn_name):
    time = timeit.timeit(
        f"{fn_name}(sum)",
        setup=(f"from __main__ import {fn_name}, sum"),
        number=1,
    )
    return time


def main():
    fastest_time = None
    fastest_fn = None

    for fn in [find_coins_greedy, find_min_coins]:
        fn_name = fn.__name__
        time = test_performance(fn_name)
        print(f"{fn_name} time: {time}")
        if not fastest_time or time < fastest_time:
            fastest_time = time
            fastest_fn = fn_name

    print(f"Fastest is {fastest_fn} with time {fastest_time} for sum=10**6")


if __name__ == "__main__":
    main()
