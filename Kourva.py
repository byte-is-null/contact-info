import time, sys

text = "Hello world!"

# First way
for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)

# Second way
for character in text:
    print(character, end="", flush=True)
    time.sleep(0.02)
