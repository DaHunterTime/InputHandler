from os import sep
import threading
import time

from inputhandler import buffer_input, get_input_buffer


def test():
    while True:
        time.sleep(5)
        buffer = get_input_buffer()
        # print("\r" + " " * len(buffer), end="\r")
        # print("HELLO!", end="\n\r")
        # print(*(char for char in buffer), sep="", end="", flush=True)
        out = "\r" + " "*len(buffer) + "\rHELLO!\n\r" + "".join(buffer)
        print(out, end="", flush=True)


thread = threading.Thread(target=test, daemon=True)
thread.start()

while True:
    try:
        buffer_input()
    except KeyboardInterrupt:
        break
