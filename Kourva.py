import itertools, time

for a, b, c in itertools.product(range(20), range(10), range(10)):
    print(a, b, c)
    time.sleep(0.02)  # 20ms delay between each character

# i put range(20) in first argument of itertools.product, so we don't need to use break
