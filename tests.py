from tests.thread_test_1 import main as thread_1


if __name__ == "__main__":
    all_funcs = {"thread 1": thread_1}
    text = ("Type the name of the test you want to run\n"
            "-----------------------------------------\n"
            "Options:\n"
            "'thread 1'\n"
            "-----------------------------------------")
    print(text)
    option = input("Select option: ")
    func = all_funcs.get("_".join(option.split()), None)

    if func is None:
        print(f"There is no test function '{option}'")
    else:
        func()
