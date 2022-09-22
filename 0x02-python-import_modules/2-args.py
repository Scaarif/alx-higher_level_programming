#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{} {}".format(len(sys.argv) - 1,
        "arguments" if len(sys.argv) != 2 else "argument"), end="")
    print("{}".format("." if len(sys.argv) == 1 else ":"))
    for index, arg in enumerate(sys.argv):
        if index != 0:
            print("{}: {}".format(index, arg))
