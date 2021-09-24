import threading
import time

from inputhandler import buffer_input, get_input_buffer, fix_cursor


def test():
    while True:
        time.sleep(5)
        buffer = get_input_buffer()
        out = "\r" + " "*len(buffer) + "\rHELLO!\n\r" + "".join(buffer)
        print(out, end="", flush=True)
        fix_cursor()  # This call is not needed in unix, but is here for Windows compatibility


def main():
    thread = threading.Thread(target=test, daemon=True)
    thread.start()

    while True:
        try:
            buffer_input()
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
